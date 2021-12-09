from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow.hooks.postgres_hook import PostgresHook

from datetime import datetime
from datetime import timedelta
import requests
import logging


def get_Redshift_connection():
    hook = PostgresHook(postgres_conn_id='redshift_dev_db')
    return hook.get_conn().cursor()


def create(**context):
    schema = context["params"]["schema"]
    table = context["params"]["table"]    

    cur = get_Redshift_connection()
    sql = \
        f"""CREATE TABLE {schema}.{table}(
                date date,
                temp float,
                min_temp float,
                max_temp float,
                created_at timestamp default sysdate
            )
        """
    logging.info(sql)
    cur.execute(sql)
    cur.execute("COMMIT;")

def extract(**context):
    #https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_key}&units=metric
    link = context["params"]["url"]
    key = context["params"]["key"]
    lat = context["params"]["lat"]
    lon = context["params"]["lon"]
    part = context["params"]["part"]

    execution_date = context['execution_date']
    logging.info(execution_date)

    
    link = link.format(lat=lat,lon=lon,part=part,API_key=key)

    f = requests.get(link)

    logging.info(f.json()['daily'][0]['dt'])
    return (f.json())

def transform(**context):
    f_json = context["task_instance"].xcom_pull(key="return_value", task_ids="extract")
    daily = f_json['daily']
    
    return daily

def load(**context):
    schema = context["params"]["schema"]
    table = context["params"]["table"]
    
    cur = get_Redshift_connection()
    daily = context["task_instance"].xcom_pull(key="return_value", task_ids="transform")

    sql = "BEGIN; DELETE FROM {schema}.{table};".format(schema=schema, table=table)

    daily = daily[1:] # 오늘 제외
    for d in daily:
        dt = datetime.fromtimestamp(d["dt"]).strftime('%Y-%m-%d')
        day = d['temp']['day']
        min = d['temp']['min']
        max = d['temp']['max']
        print(f"date : {dt} temp_day : {day} temp_min : {min} temp_max : {max}")
        sql += f"""INSERT INTO {schema}.{table} VALUES ('{dt}', '{day}', '{min}', '{max}');"""
    sql += "END;"

    logging.info(sql)
    cur.execute(sql)
    cur.execute("COMMIT;")



dag_weather_forecast = DAG(
    dag_id = 'dag_weather_forecast',
    start_date = datetime(2021,11,27), # 날짜가 미래인 경우 실행이 안됨
    schedule_interval = '0 2 * * *',  # 적당히 조절
    max_active_runs = 1,
    catchup = False,
    default_args = {
        'retries': 1,
        'retry_delay': timedelta(minutes=3),
    }
)

create = PythonOperator(
    task_id = 'create',
    python_callable = create,
    params = {
        'schema': 'sosb0421',   ## 자신의 스키마로 변경
        'table': 'weather_forecast',
    },
    provide_context=True,
    dag = dag_weather_forecast)


extract = PythonOperator(
    task_id = 'extract',
    python_callable = extract,
    params = {
        'url':  Variable.get("open_weather_api_url"),
        'key':  Variable.get("open_weather_api_key"),
        'lat':  37.5665,
        'lon':  126.978,
        'part': 'current'
    },
    provide_context=True,
    dag = dag_weather_forecast)

transform = PythonOperator(
    task_id = 'transform',
    python_callable = transform,
    params = { 
    },  
    provide_context=True,
    dag = dag_weather_forecast)

load = PythonOperator(
    task_id = 'load',
    python_callable = load,
    params = {
        'schema': 'sosb0421',   ## 자신의 스키마로 변경
        'table': 'weather_forecast',
    },
    provide_context=True,
    dag = dag_weather_forecast)


create >> extract >> transform >> load