import stu_func

students = [
    {"no":1,"name":"Eric","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":0},
    {"no":2,"name":"Hina","kor":70,"eng":90,"math":90,"total":250,"avg":83.33,"rank":0},
    {"no":3,"name":"Nicky","kor":60,"eng":100,"math":60,"total":220,"avg":73.33,"rank":0},
]
count = 4
title =['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    try:
        stu_func.stu_print()
        choice = int(input("원하는 번호를 입력하세요.>> "))
        if choice == 1:
            count=stu_func.stu_input(count,students)
        elif choice == 2:
            stu_func.stu_output(students)
        elif choice == 3:
            stu_func.stu_adjust(students)
        elif choice == 4:
            stu_func.stu_delete(students)
        elif choice == 5:
            print("[ 학생성적 정렬 ]")
        elif choice == 6:
            stu_func.stu_search(students)
        elif choice == 7:
            stu_func.stu_rank(students)
        elif choice == 0:
            print(" [ 프로그램 종료 ]")
            break
    except :
        print("잘못 입력하였습니다.")
        continue