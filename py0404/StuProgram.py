from StuFunc import*

students = []

with open("py0404/stu.txt","r",encoding="utf8")as f:
    while True:
        line = f.readline()
        if not line: break
        s = line.strip().split(",")
        students.append({"no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])})

title =['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    try:
        stu_print()
        choice = int(input("원하는 번호를 입력하세요.>> "))
        if choice == 1:
            stu_input(students) #입력
        elif choice == 2:
            stu_output(students) #출력
        elif choice == 3:
            stu_adjust(students) #수정
        elif choice == 4:
            stu_delete(students) #삭제
        elif choice == 5:
            stu_array(students) #정렬
        elif choice == 6:
            stu_search(students) #검색
        elif choice == 7:
            stu_rank(students) #등수처리 
        elif choice == 8:
            stu_save(students) #저장
        elif choice == 0:
            print(" [ 프로그램 종료 ]") #종료
            break
    except :
        print("잘못 입력하였습니다.")
        continue