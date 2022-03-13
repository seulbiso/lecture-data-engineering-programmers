# lecture-data-engineering-programmers
[스터디/6기] 실리콘밸리에서 날아온 데이터 엔지니어링 스타터 키트 with Python

### 강의 내용 및 실습
1.SQL의 이해 (1~3 주차)
- SQL 기본 개념 및 Redshift 통한 SQL 실습

2.Airflow 설치 (4주차)
- AWS EC2에 Airflow 설치
- Airflow 메타데이터베이스로 로컬 서버에 Postgres를 설치

3.Airflow를 통한 주간 날씨 정보 받아오기 (5주차)
- Open Weathermap API : 위도/경도를 기반으로 그 지역의 기후 정보를 알려주는 서비스
- 무료 계정으로 api key를 받아서 이를 호출시에 사용
  https://openweathermap.org/price
- 특정 날짜 이후 일주일 날씨 정보 받아오기
- 실습 소스 : https://github.com/seulbiso/lecture-data-engineering-programmers/blob/7d3c55d3a69453ebf88a4ac0fb6938f9434c4882/week5/dags/Weather_Forecast.py


4.Airflow로 ETL 구현
- Product DB (MySQL)에서 S3로 SQL 실행 결과 파일로 지속적으로 업로드
- S3에서 Redshift로 Bulk insert
![image](https://user-images.githubusercontent.com/43867643/158063017-976eacf3-e7bf-4e1a-8fc0-b66cc0aef019.png)
- 실습 소스 : https://github.com/seulbiso/lecture-data-engineering-programmers/blob/7d3c55d3a69453ebf88a4ac0fb6938f9434c4882/week6/Build_Summary.py
