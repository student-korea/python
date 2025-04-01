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
        print("[ 학생성적 입력 ]")
        no = count
        name = input("이름을 입력하세요. ")
        kor = int (input("국어 점수를 입력하세요. "))
        eng = int (input("영어 점수를 입력하세요. "))
        math = int (input("수학점수를 입력하세요. "))
        total = kor+eng+math
        avg = total/3
        rank=0
        student = [no,name,kor,eng,math,total,avg,rank]
        students.append(student)
        print(f"{no}번 {name}학생 성적이 등록되었습니다.")
        count+=1
        
    elif choice == 2:
        print("[ 학생성적 출력 ]")
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
        print("[ 학생성적 수정 ]")
        name=input("수정하려고 하는 학생 이름을 입력하세요.>>")
        temp=0 #찾지 못할경우 사용
        for i,s in enumerate(students):
            if name in s: #있을 경우
                temp=1
                print(f"{name}학생을 찾았습니다.")
                print()
                print(" [ 수정하려는 과목 선택 ]")
                print(" 1. 국어")
                print(" 2. 영어")
                print(" 3. 수학")
                print(" 0. 취소")
                choice=int(input("/원하는 번호를 입력하세요. "))
                if choice == 1:
                    print(" [ 국어성적 수정 ]")
                    print(f"현재 국어점수 : {s[2]}")
                    s[2] = int(input("변경 국어점수 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name}학생 성적이 수정되었습니다.")
                elif choice == 2:
                    print(" [ 영어성적 수정 ]")
                    print(f"현재 영어점수 : {s[3]}")
                    s[3] = int(input("변경 영어점수 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name}학생 성적이 수정되었습니다.")
                elif choice == 3:
                    print(" [ 수학성적 수정 ]")
                    print(f"현재 수학점수 : {s[4]}")
                    s[4] = int(input("변경 수학점수 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name}학생 성적이 수정되었습니다.")
                else:
                    print(f"{name}학생 성적수정을 취소했습니다.")
        if temp==0:
            print(f"{name} 학생을 찾지못했습니다. 다시 실행해주세요.")
            
    elif choice == 4:
        print("[ 학생성적 삭제 ]")
        name=input("삭제하려고 하는 학생 이름을 입력하세요.>>")
        temp=0
        for i,s in enumerate(students):
            if name in s: #있을 경우
                temp=1
                print(f"{name}학생을 찾았습니다.")
                choice=int(input(f"{name}학생성적을 삭제할까요?(0.취소,1.삭제)"))
                if choice == 1:
                    del students[i]
                    print(f"{name}학생 성적을 삭제했습니다.")
                else:
                    print(f"{name}학생 성적삭제를 취소햇습니다.")
                break
        if temp==0:
            print(f"{name}학생을 찾지못했습니다. 다시 실행해주세요.")
            
    elif choice == 5:
        print("[ 학생성적 정렬 ]")
        students.sort()
    elif choice == 6:
        print("[ 학생성적 검색 ]")
    elif choice == 7:
        print("[ 등수 처리 ]")
    else :
        print("[ 프로그램 종료 ]")
        break
    print()