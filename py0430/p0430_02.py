import dbconn

print("---------db연결--------")
conn =dbconn.connections()
cursor = conn.cursor()
cursor.execute("select employee_id,emp_name,salary from employees where salary between 4000 and 6000")
rows = cursor.fetchall()

name = input("검색하려는 이름을 입력하세요.>> ")
name = '%'+name+'%'
query = "select employee_id,emp_name,salary from employees where emp_name like :name "

cursor.execute(query,name=name) #sql구문 F9실행
rows = cursor.fetchall()  # 데이터를 가져옴.

for r in rows:
    print(r[0],r[1],r[2])
