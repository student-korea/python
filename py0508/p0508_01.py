import oracledb

def connections():
    try: conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn
conn = connections()
cursor = conn.cursor()
while True:
    print("[학생 성적 프로그램]")
    print("1. 학생 전체 출력")
    print("2. 학반별 최고등수 출력")
    print("3. 학반별 촤하등수 출력")
    print("4. 부서별 최고연봉 출력")
    print("5. stuscore2 학반 부여")
    print("6. 회원정보 rownum을 사용 ")
    print("0. 프로그램 종료 ")
    print("-"*20)
    choice = input("원하는 번호를 입력하세요.>> ")
    if choice == "1":
        query ='select * from stuscore2'
        cursor.execute(query)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print()
    elif choice == "2":
        query ='select sno,name,total,sclass from stuscore a\
            where total in (select max(total) maxtotal from stuscore b\
            where a.sclass = b.sclass group by sclass)' 
        cursor.execute(query)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print()
    elif choice == "3":
        query ='select sno,name,total,sclass from stuscore a\
            where total in (select min(total) mintotal from stuscore b\
            where a.sclass = b.sclass group by sclass)' 
        cursor.execute(query)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print()
    elif choice == "4":
        query ='select employee_id,emp_name,salary,department_id from employees a\
            where salary in (select max(salary) maxsalary from employees b\
            where a.department_id = b.department_id group by department_id)' 
        cursor.execute(query)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print()
    elif choice == "5":
        query ='update stuscore2 set sclass=\
                case\
                    when sno between 1 and 10 then 1\
                    when sno between 11 and 20 then 2\
                    when sno between 21 and 30 then 3\
                    when sno between 31 and 40 then 4\
                    when sno between 41 and 50 then 5\
                    when sno between 51 and 60 then 6\
                    when sno between 61 and 70 then 7\
                    when sno between 71 and 80 then 8\
                    when sno between 81 and 90 then 9\
                    when sno between 91 and 100 then 10\
                    else 11\
                end' 
        cursor.execute(query)
    elif choice == "6":
        num1 = int(input("num1 "))
        num2 = int(input("num2 "))
        query =f'select sno,name,kor,eng,math,total,avg,rank,sgrade,sclass from (select rownum rnum,a.* from stuscore2 a) where rnum between {num1} and {num2}' 
        cursor.execute(query)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print()
    elif choice == "0":
        break
    
cursor.close()    
conn.close() 