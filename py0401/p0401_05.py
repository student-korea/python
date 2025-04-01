students = [
    [1,"Eric",100,100,100,300,100,1],
    [2,"Hina",70,90,90,250,83.33,3],
    [3,"Casper",100,90,80,270,90,2]
]
student = []
print("*"*30)
print(" "*5,end="")
print("[ 학생 성적 프로그램 ]")
print("*"*30)
count = 4
while True:
    print("1.학생성적 입력")
    print("2.학생성적 출력")
    print("3.학생성적 수정")
    print("4.학생성적 삭제")
    print("5.학생성적 정렬")
    print("6.학생성적 검색")
    print("7.등수처리")
    print("0.프로그램 종료")
    print("*"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    if choice == 1:
        print("[학생성적 입력]")
        no = count
        name = input("이름")
        kor = int(input("국어"))
        eng = int(input("영어"))
        math = int(input("수학"))
        total = kor+eng+math
        aver = total/3
        rank = 0
        student=[no,name,kor,eng,math,total,aver,rank]
        students.append(student)
        count+=1
        print()
        
    elif choice == 2:
        print("[학생성적 출력]")
        print("          [ 학생성적 프로그램 ]")
        print("-"*65)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        print("-"*65)
        for stu in students:
            for i,s in enumerate(stu):
                if i !=6:
                    print(s,end="\t")
                else :
                    print(f"{s:.2f}",end="\t")
            print()
        print()
    elif choice == 3:
        print("[학생성적 수정]")
        name = input("수정이름 입력 : ")
        temp = 0
        for i,s in enumerate(students):
            if name in s:
                temp +=1
                print(f"{name}찾음")
                print("수정과목 선택")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 취소")
                choice = int(input("입력"))
                if choice == 1:
                    print("국어수정")
                    print(f"현재 국어점수 : {s[2]}")
                    s[2] = int(input("변경 국어점수 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                elif choice == 2:
                    print("영어수정")
                    print(f"현재 영어점수 : {s[3]}")
                    s[3] = int(input("변경 영어점수 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                elif choice == 3:
                    print("수학수정")
                    print(f"현재 수학점수 : {s[4]}")
                    s[4] = int(input("변경 수학점수 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                else:
                    break
        if temp==0:
            print("못찾음 다시하셈")
            print()   
    elif choice == 4:
        print("[학생성적 삭제]")
        name = input("삭제이름 입력 : ")
        temp = 0
        for i,s in enumerate(students):
            temp +=1
            if name in s:
                print(f"{name}찾음")
                choice = int(input(f"{name}을 삭제하겠습니다. (0. 취소, 1. 삭제)"))
                if choice == 1:
                    del students[i]
                    print("삭제 완료")
                else:
                    break
        if temp==0:
            print("못찾음 다시하셈")
            print()
    else :
        break