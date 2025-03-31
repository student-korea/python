students = list()
student = []
print("*"*30)
print(" "*5,end="")
print("[ 학생 성적 프로그램 ]")
print("*"*30)
count = 1
while True:
    print("1.학생성적 입력")
    print("2.학생성적 출력")
    print("3.학생성적 수정")
    print("4.학생성적 삭제")
    print("5.학생성적 정렬")
    print("6.학생성적 검색")
    print("0.프로그램 종료")
    print("*"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    if choice == 1:
        print("[ 학생성적 입력]")
        no = count
        name = input("What's your name? ")
        kor = int (input("korea score? "))
        eng = int (input("english score? "))
        math = int (input("math score? "))
        total = kor+eng+math
        avg = total/3
        rank=0
        student = [no,name,kor,eng,math,total,avg,rank]
        students.append(student)
        count+=1
    elif choice == 2:
        print("[ 학생성적 출력]")
        print("               [ 학생성적 프로그램 ]")
        print("-"*65)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        print("-"*65)
        for stu in students:
            for i,s in enumerate(stu):
                if i!=6: 
                    print(s,end="\t")
                else:
                    print(f"{s:.2f}",end="\t")
            print()
    elif choice == 3:
        print("[ 학생성적 수정]")
    elif choice == 4:
        print("[ 학생성적 삭제]")
    elif choice == 5:
        print("[ 학생성적 정렬]")
    elif choice == 6:
        print("[ 학생성적 검색]")
    elif choice == 0:
        print("[ 프로그램 종료]")
        break
    print()