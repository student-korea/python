### 학생성적 프로그램
### 진행하세요.

print("-"*40)
students = [
    {"no":1,"name":"Eric","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
    {"no":2,"name":"Hina","kor":70,"eng":90,"math":90,"total":250,"avg":83.33,"rank":3},
    {"no":3,"name":"Rei","kor":100,"eng":90,"math":80,"total":270,"avg":90,"rank":2},
]

count = 4
title =['번호','이름','국어','영어','수학','합계','평균','등수']

while(True):
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
    if choice == 0:
        print("프로그램 종료")
        break
    elif choice == 1:
        print(" "*18,end="")
        print("[학생성적 입력]")
        print("*"*60)
        while True:
            no=count
            name = input(f"{no}번 이름을 입력하세요.(0.이전화면 이동)>> ")
            if name == '0': break
            kor=int(input("국어점수를 입력하세요. "))
            eng=int(input("영어점수를 입력하세요. "))
            math=int(input("수학점수를 입력하세요. "))
            total=kor+eng+math
            avg = total/3.0
            rank=0
            students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
            count+=1
            print(f"{name}님이 등록되었습니다.")
            print()
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
        print(" "*18,end="")
        print("[학생성적 수정]")
        print("*"*60)
        while True:
            name = input(f"수정하고자 하는 이름을 입력하세요.(0.이전화면 이동)>> ")
            if name == '0': break
            temp=0
            for s in  students:
                if name in s["name"]:
                    temp+=1
                    print(f"{name}을 찾았습니다.")
                    print(" [ 수정하려는 과목 선택 ]")
                    print(" 1. 국어")
                    print(" 2. 영어")
                    print(" 3. 수학")
                    print(" 0. 취소")
                    choice=int(input("원하는 번호를 입력하세요. "))
                    if choice==0:
                        print("취소하였습니다.")
                        break
                    elif choice == 1:
                        print(" [ 국어성적 수정 ]")
                        print(f"현재 국어점수 : {s["kor"]}")
                        s["kor"] = int(input("변경 국어점수 : "))
                        s["total"] = s["kor"]+s["eng"]+s["math"]
                        s["avg"] = s["total"]/3
                        print(f"{name}학생 성적이 수정되었습니다.")
                    elif choice==2:
                        print(" [ 영어성적 수정 ]")
                        print(f"현재 영어점수 : {s["eng"]}")
                        s["eng"] = int(input("변경 영어점수 : "))
                        s["total"] = s["kor"]+s["eng"]+s["math"]
                        s["avg"] = s["total"]/3
                        print(f"{name}학생 성적이 수정되었습니다.")
                    elif choice==3:
                        print(" [ 수학성적 수정 ]")
                        print(f"현재 수학점수 : {s["math"]}")
                        s["math"] = int(input("변경 수학점수 : "))
                        s["total"] = s["kor"]+s["eng"]+s["math"]
                        s["total"] = s["avg"]/3
                        print(f"{name}학생 성적이 수정되었습니다.")
            if temp==0:
                print(f"{name}학생을 찾지 못하였습니다. 다시 시도해보세요.")
                break
    elif choice == 4:
        print(" "*18,end="")
        print("[학생성적 삭제]")
        print("*"*60)
        while True:
            name = input(f"삭제하고자 하는 이름을 입력하세요.(0.이전화면 이동)>> ")
            if name == '0': break
            temp=0
            for i,s in enumerate(students):
                if name in s["name"]:
                    temp+=1
                    print(f"{name}을 찾았습니다.")
                    print(f"{name}학생을 삭제하시겠습니까? ")
                    print(" 1. 삭제")
                    print(" 0. 취소")
                    choice=int(input("원하는 번호를 입력하세요. "))
                    if choice==0:
                        print("취소하였습니다.")
                        break
                    elif choice == 1:
                        del students[i]
                        print(f"{name}학생 성적이 삭제되었습니다.")
            if temp==0:
                print(f"{name}학생을 찾지 못하였습니다. 다시 시도해보세요.")
                break
    elif choice == 5:
        print(" "*18,end="")
        print("[학생성적 정렬]")
        print("*"*60)
        while True:
            print("[ 학생성적 정렬 ]")
            print("1. 이름 순차정렬")
            print("2. 이름 역순정렬")
            print("3. 합계 순차정렬")
            print("4. 합계 역순정렬")
            print("5. 번호 순차정렬")
            print("6. 번호 역순정렬")
            print("0. 이전화면이동")
            print("-"*30)
            students2 = [*students]
            choice=int(input("원하는 번호를 입력하세요.(0. 취소)>> "))
            if choice==1:
                students2.sort(key=lambda x:x['name'])
            elif choice==2:
                students2.sort(key=lambda x:x['name'],reverse=True)
            elif choice==3:
                students2.sort(key=lambda x:x['total'])
            elif choice==4:
                students2.sort(key=lambda x:x['total'],reverse=True)
            elif choice==5:
                students2.sort(key=lambda x:x['no'])
            elif choice==6:
                students2.sort(key=lambda x:x['no'],reverse=True)
            elif choice==0:
                break
            print(" "*18,end="")
            print("[ 학생 성적 프로그램 ]")
            print("*"*60)
            print(f"{title[0]}\t{title[1]}\t{title[2]}\t{title[3]}\t{title[4]}\t{title[5]}\t{title[6]}\t{title[7]}")
            print("*"*60)
            for s in students2:
                print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
            print()
    elif choice == 6:
        print(" "*18,end="")
        print("[학생성적 검색]")
        print("*"*60)
        while True:
            name = input(f"검색하고자 하는 이름을 입력하세요.(0.이전화면 이동)>> ")
            if name == '0': break
            temp=0
            for i,s in enumerate(students):
                if name in s["name"]:
                    temp+=1
                    print(" "*22,end="")
                    print(f"[ {name} 성적 ]")
                    print("*"*60)
                    print(f"{title[0]}\t{title[1]}\t{title[2]}\t{title[3]}\t{title[4]}\t{title[5]}\t{title[6]}\t{title[7]}")
                    print("*"*60)
                    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
                    print()
                    break
            if temp==0:
                print(f"{name}학생을 찾지 못하였습니다. 다시 시도해보세요.")
                break
    elif choice == 7:
        print("[등수처리]")
        for s in students:
            num = 1
            for ss in students:
                if s["total"]<ss["total"]:
                    num+=1
            s["rank"]=num
        print("등수 처리 완료")    
    elif choice == 8:
        print("[학생성적 저장]")
        with open("py0430/stu.txt","w",encoding="utf8") as f:
            for s in students:
                line = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']:.2f},{s['rank']}\n"
                f.write(line)
        print("파일이 저장되었습니다")
