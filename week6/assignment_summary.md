# Assessment 1
![assessment1](https://user-images.githubusercontent.com/43867643/146570546-83576e2f-884d-41f8-b8f2-5688c0e6def7.PNG)

# Assessment 2
![assessment2](https://user-images.githubusercontent.com/43867643/146570594-451369b7-3216-4132-b6d4-428938acec37.PNG)

# Assessment 3
1. SQL
 ```
SELECT 
    DATE(created_at) as date,
    100 * (count(CASE WHEN score >= '9' THEN 1 END) - count(CASE WHEN score <= '6' THEN 1 END)) / count(score)  as nps
FROM sosb0421.nps 
WHERE DATE(created_at) = DATE('{execution_date}')
GROUP BY DATE(created_at);
 ```
2. CODE
- https://github.com/padakpadak/lecture-data-engineering-programmers/blob/b79d4ad7b4c9385ee0c8ec7ea7dd8dbdb2cf439a/week6/Build_Summary.py

3. Result
![image](https://user-images.githubusercontent.com/43867643/146573969-28d66b70-e389-4a90-be52-c38067f646e8.png)
