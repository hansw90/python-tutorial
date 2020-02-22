import pymysql
 
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='root',
                       db='world', charset='utf8')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 
# SQL문 실행
sql = "select * from city"
curs.execute(sql)
 
# 데이타 Fetch
rows = curs.fetchall()
print(rows)     # 전체 rows
# print(rows[0])  
# print(rows[1])  
 
# Connection 닫기
conn.close()
