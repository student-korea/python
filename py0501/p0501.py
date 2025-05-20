
from dbconn import *



conn=connections()
cursor = conn.cursor()

while True:
    print(" "*20)
    print('[ 학생성적처리 프로그램]')
    print("-"*30)
    print("1.학생성적 입력")
    print("2.학생성적 출력")
    print("3.학생성적 수정")
    print("4.학생성적 삭제")
    print("5.학생성적 정렬")
    print("6.학생성적 검색")
    print("7.등수처리")
    print("8.학생성적 저장")
    print("0.프로그램 종료")
    print("*"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 0: break
    elif choice == 1:
        print(" "*18,end="")
        print("[학생성적 입력]")
        print("*"*60)
        while True:
            name = input("이름을 입력하세요.(0.이전화면 이동)>> ")
            if name == '0': break
            kor=int(input("국어점수를 입력하세요. "))
            eng=int(input("영어점수를 입력하세요. "))
            math=int(input("수학점수를 입력하세요. "))
            total=kor+eng+math
            avg = total/3.0
            query = "insert into stuscore values(stuscore_seq.nextval,:name,:kor,:eng,:math,:total,:avg,0)"
            cursor.execute(query,name=name,kor=kor,eng=eng,math=math,total=total,avg=avg)
            conn.commit()
            print(f"{name}님이 등록되었습니다.")
            print()
    elif choice == 2:
        query ='select * from stuscore'
        cursor.execute(query)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print()
        
    elif choice == 3:
        kor=int(input("국어점수를 입력하세요. "))
            
        query="update stuscore set kor=:kor,total=:kor+eng+math, avg=(:kor+eng+math)/3.0 where sno=105"
        cursor.execute(query,kor=kor)
        conn.commit
        print("수정이 되었습니다.")
        
    elif choice == 5:
        query="select * from stuscore order by name desc"
        cursor.execute(query)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print()
        
    elif choice == 6:
        name = input("이름을 입력하세요.(0.이전화면 이동)>> ")
        if name == '0': break
        query ="select * from stuscore where name like '%'||:name||'%'"
        cursor.execute(query,name=name)
        rows = cursor.fetchall()
        if len(rows) <=0:
            print("없음")
            continue
        for r in rows:
            print(r)
        print()
        
conn.close()

print("[프로그램 종료]")
# query = 'select count(*) from stuscore'
# cursor.execute(query)
# cnt = cursor.fetchall()
# print("학생수 : ",cnt[0][0])
# # cnt = cursor.fetchone()
# # print("학생수 : ",cnt[0])


# query ='select * from stuscore'
# cursor.execute(query)
# rows = cursor.fetchall()
# for r in  rows:
#     print(r)
# conn.close()