# ASSIGNMENT 1
- week5/dags/NameGenderCSVtoRedshift.py
- week5/dags/NameGenderCSVtoRedshift2.py
- week5/dags/NameGenderCSVtoRedshift3.py
- week5/dags/NameGenderCSVtoRedshift4.py
# ASSIGNMENT 2
- week5/dags/Weather_Forecast.py
## 결과
![image](https://user-images.githubusercontent.com/43867643/145414902-3b20d899-bfae-4bd5-8830-e28088accdbb.png)

# ASSIGNMENT 3
1. Airflow의 환경 설정이 들어있는 파일의 이름은?
  - Airflow 환경 파일(/var/lib/airflow/airflow.cfg)
2. 이 파일에서 DAG의 스케줄에 사용되는 타임존을 바꾸려면 어느 섹션을 변경해야하는지?
  - airflow.cfg
  ```
  [core]
  ...
  ...
  # default_timezone = utc
  default_timezone = Asia/Seoul
  ````
3. 이 파일에서 Airflow를 API 형태로 외부에서 조작하고 싶다면 어느 섹션을 변경해야하는가?
  - airflow.cfg
  ```
  [core]
  ...
  ...
  # airflow.cfg 설정 변경 
  auth_backend = airflow.api.auth.backend.basic_auth
  
  출처: https://118k.tistory.com/1067 [개발자로 살아남기]
  ````
4. Variable에서 변수의 값이 encrypted가 되려면 변수의 이름에 어떤 단어들이 들어가야 하는데 이 단어들은 무엇일까?
  - Password, API Key
5. 이 환경 설정 파일이 수정되었다면 이를 실제로 반영하기 위해서 해야 하는 일은?
  - Airflow 재설정
  ```
  AIRFLOW_HOME=/var/lib/airflow airflow db init
  ```
