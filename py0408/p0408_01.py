title =['번호','이름','국어','영어','수학','합계','평균','등수']
while True:
    print("1. 국어입력")
    print("2. 영어입력")
    print("3. 수학입력")
    choice = int(input("원하는 번호를 입력하시오.>> "))
    print(f"[{title[choice+1]} 성적 입력]")
    