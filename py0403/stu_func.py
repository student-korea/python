def stu_print():
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

def stu_input(count,students):
    while True:
            print(" [ 학생성적 입력 ]")
            no = count
            name = input(f"{no}번 학생 이름을 입력하세요.(0. 이전화면으로 이동)>> ")
            if name == "0": break
            name = name.title()
            score = [0]*3
            score_cal(0,score)
            score_cal(1,score)
            score_cal(2,score)
            total = score[0]+score[1]+score[2]
            avg = total/3
            rank = 0
            students.append({"no":no,"name":name,"kor":score[0],"eng":score[1],"math":score[2],"total":total,"avg":avg,"rank":rank})
            print(f"{name}학생성적이 등록되었습니다.")
            print()
            count+=1
            return count
            
def score_cal(i,score):
    while 1:
        score[i] = input(f"{title[i+2]}점수를 입력하세요.>> ")
        if score[i].isdigit(): 
            score[i]=int(score[i])
            if 0<=score[i]<=100: break
            else: print(" 점수는 0~100 까지 가능합니다.")
        else : print("숫자를 입력하세요.")
        
def stu_output(students):
    print(" "*18,end="")
    print("[ 학생 성적 프로그램 ]")
    print("*"*60)
    print(f"{title[0]}\t{title[1]}\t{title[2]}\t{title[3]}\t{title[4]}\t{title[5]}\t{title[6]}\t{title[7]}")
    print("*"*60)
    for s in students:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()
        
title =['번호','이름','국어','영어','수학','합계','평균','등수']

def stu_adjust(students):
    while 1:
        print("[ 학생성적 수정 ]")
        name = input("수정하려고 하는 학생이름을 입력하세요.(0.이전 화면 이동)>> ")
        if name == "0": break
        name = name.title()
        temp = 0
        for s in students:
            if name in s['name']:
                temp += 1
                print(f"{name} 학생이 있습니다. 성적을 수정합니다.")
                print("[ 수정할 과목 선택 ]")
                print(" 1. 국어")
                print(" 2. 영어")
                print(" 3. 수학")
                print("-"*30)
                choice=int(input("원하는 번호를 입력하세요.>> "))
                score_adjust(choice,s,name)
                print()
        if temp==0:
            print(f"{name} 학생을 찾지못했습니다. 다시 실행해주세요.")
            print()
            
def score_adjust(i,s,name):
    sub_list = [' ',"kor", "eng", "math"][i]
    print(f" [ {title[i+1]}성적 수정 ]")
    print(f"현재 {title[i+1]}점수 : {s[sub_list]}")
    pre_score = s[sub_list]
    s[sub_list] = int(input(f"변경 {title[i+1]}점수 : "))
    s['total'] = s['kor']+s['eng']+s['math']
    s['avg'] = s['total']/3
    print(f"{name}학생의 {title[i+1]}성적이 {pre_score}점에서 {s[sub_list]}점으로 수정되었습니다.")

def stu_delete(students):
    while True:
        print("[ 학생성적 삭제 ]")
        name = input("삭제하려고 하는 학생이름을 입력하세요.(0.이전 화면 이동)>> ")
        if name == "0": break
        name = name.title()
        temp=0
        for i,s in enumerate(students):
            if name in s['name']: #있을 경우
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

def stu_search(students):
    print("[ 학생성적 검색 ]")
    while True:
        name = input("검색하려고 하는 학생이름을 입력하세요.(0.이전 화면 이동)>> ")
        if name == "0": break
        name = name.title()
        temp = 0
        for s in students:
            if name in s['name']:
                temp += 1
                print("*"*60)
                print(f"{title[0]}\t{title[1]}\t{title[2]}\t{title[3]}\t{title[4]}\t{title[5]}\t{title[6]}\t{title[7]}")
                print("*"*60)
                print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
                break
        if temp==0:
            print(f"{name}학생을 찾지못했습니다. 다시 실행해주세요.")

def stu_rank(students):
    print("[ 등수처리 ]")
    for s in students:
        num = 1 
        for ss in students:
            if s['total']<ss['total']:
                num +=1
        s['rank'] = num
    print("등수 처리 완료")
    print()