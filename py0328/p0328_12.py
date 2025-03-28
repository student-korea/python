# while True:
#     num = int(input("숫자를 입력하세요. "))
#     if num == 0:
#         break

while True:
    print("[ 프로그램 구현 ]")
    print("-"*20)
    print("1. 숫자맞추기")
    print("2. 로또맞추기")
    print("3. 학생성적 프로그램")
    print("0. 종료")
    choice = int(input("원하는 번호를 입력하세요.  "))
    
    if choice == 1:
        print("[ 숫자 맞추기 프로그램 ]")
    elif choice == 2:
        print("[ 로또 맞추기 프로그램 ]")
    elif choice == 3:
        print("[ 학생성적 프로그램 ]")
    elif choice == 0:
        print("[ 종료 ]")
        break
    else :
        print("다시 입력하세요.")
