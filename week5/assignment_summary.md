# ASSIGNMENT 1
## 과제
숙제 1: 오늘 설명한 내용들 따라해보기
- Transaction 실습 따라하기
- Name Gender 실습 따라하기


## 결과
- [week5/dags/NameGenderCSVtoRedshift.py](https://github.com/padakpadak/lecture-data-engineering-programmers/blob/e5ec8b9234bdf0ce7c5be0cb6e4dee81e91f40b9/week5/dags/NameGenderCSVtoRedshift.py)
- [week5/dags/NameGenderCSVtoRedshift_v2.py](https://github.com/padakpadak/lecture-data-engineering-programmers/blob/e5ec8b9234bdf0ce7c5be0cb6e4dee81e91f40b9/week5/dags/NameGenderCSVtoRedshift_v2.py)
- [week5/dags/NameGenderCSVtoRedshift_v3.py](https://github.com/padakpadak/lecture-data-engineering-programmers/blob/e5ec8b9234bdf0ce7c5be0cb6e4dee81e91f40b9/week5/dags/NameGenderCSVtoRedshift_v3.py)
- [week5/dags/NameGenderCSVtoRedshift_v4.py](https://github.com/padakpadak/lecture-data-engineering-programmers/blob/e5ec8b9234bdf0ce7c5be0cb6e4dee81e91f40b9/week5/dags/NameGenderCSVtoRedshift_v4.py)
# ASSIGNMENT 2
## 과제
숙제 2: Weather_Forecast DAG 구현해보기
- 앞서 설명한 Open Weather DAG를 실제로 구현하기
```
FULL REFRESH 형태로  구현해보기
API Key는 어디에 저장해야할까?
DW상의 테이블은 아래처럼 정의
CREATE TABLE 각자스키마.weather_forecast (
    date date primary key,
    temp float,
    min_temp float,
    max_temp float,
    created_date timestamp default GETDATE()
);
```
## 결과
- [week5/dags/Weather_Forecast.py](https://github.com/padakpadak/lecture-data-engineering-programmers/blob/e5ec8b9234bdf0ce7c5be0cb6e4dee81e91f40b9/week5/dags/Weather_Forecast.py)
![image](https://user-images.githubusercontent.com/43867643/145414902-3b20d899-bfae-4bd5-8830-e28088accdbb.png)

# ASSIGNMENT 3
### 1. Airflow의 환경 설정이 들어있는 파일의 이름은?
  - Airflow 환경 파일(/var/lib/airflow/airflow.cfg)
### 2. 이 파일에서 DAG의 스케줄에 사용되는 타임존을 바꾸려면 어느 섹션을 변경해야하는지?
  - airflow.cfg
  ```
  [core]
  ...
  ...
  # default_timezone = utc
  default_timezone = Asia/Seoul
  ````
### 3. 이 파일에서 Airflow를 API 형태로 외부에서 조작하고 싶다면 어느 섹션을 변경해야하는가?
  - airflow.cfg
  ```
  [core]
  ...
  ...
  # airflow.cfg 설정 변경 
  auth_backend = airflow.api.auth.backend.basic_auth
  
  출처: https://118k.tistory.com/1067 [개발자로 살아남기]
  ````
### 4. Variable에서 변수의 값이 encrypted가 되려면 변수의 이름에 어떤 단어들이 들어가야 하는데 이 단어들은 무엇일까?
  - Password, API Key
### 5. 이 환경 설정 파일이 수정되었다면 이를 실제로 반영하기 위해서 해야 하는 일은?
  - Airflow 재설정
  ```
  AIRFLOW_HOME=/var/lib/airflow airflow db init
  ```
