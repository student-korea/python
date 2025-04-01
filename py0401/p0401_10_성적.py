students = [
    {"no":1,"name":"Eric","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
    {"no":2,"name":"Hina","kor":70,"eng":90,"math":90,"total":250,"avg":83.33,"rank":3},
    {"no":3,"name":"Casper","kor":100,"eng":90,"math":80,"total":270,"avg":90,"rank":2},
]
print(students[0])
count = 4
title =['번호','이름','국어','영어','수학','합계','평균','등수']
while True:
    print(" "*4,end="")
    print("[ 학생 성적 프로그램 ]")
    print("*"*30)
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
    if choice == 1:
        while True:
            print("[ 학생 성적 입력 ]")
            no = count
            name = input(f"{no}번 이름을 입력하세요.(0.이전화면 이동)>> ")
            if name == '0': break
            kor = int (input("국어점수를 입력하세요. "))
            eng = int (input("영어점수를 입력하세요. "))
            math = int (input("수학점수를 입력하세요. "))
            # score = [0]*3
            # for i in range(3):
            #     score[i] = int (input(f"{title[i+2]}점수를 입력하세요. "))
            total = kor+eng+math
            avg = total/3
            rank=0
            students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
            print(f"{name}이 등록되었습니다.")
            print()
            count+=1
    elif choice == 2:
        print(" "*18,end="")
        print("[ 학생 성적 프로그램 ]")
        print("*"*60)
        print(f"{title[0]}\t{title[1]}\t{title[2]}\t{title[3]}\t{title[4]}\t{title[5]}\t{title[6]}\t{title[7]}")
        print("*"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
    elif choice == 3:
        print("[ 학생성적 수정 ]")
        name=input("수정하려고 하는 학생 이름을 입력하세요.>>")
        temp= 0
        for i,s in enumerate (students):
            if name in students:
                print(f"{name}학생을 찾았습니다.")
                print()
                print(" [ 수정하려는 과목 선택 ]")
                print(" 1. 국어")
                print(" 2. 영어")
                print(" 3. 수학")
                print(" 0. 취소")
                choice=int(input("원하는 번호를 입력하세요. "))
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
    else :
        print("[ 프로그램 종료 ]")
        break
            