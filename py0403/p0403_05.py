# 로또 프로그램
# 6개 숫자 랜덤 번호 생성
# 6개 입력한 번호 생성
# 당첨번호 확인
# 출력
# 숫자맞추기 프로그램
import random
lotto = random.sample(range(1,45+1),6)
lotto2 = [i+1 for i in range(45)]
my_lotto = [0]*6
win_lotto = []
def mix_lotto():
    global lotto
    lotto = random.sample(range(1,45+1),6)
while True:
    mix_lotto()
    print("[ 로또 프로그램 ]")
    print("-"*30)
    print("1. 로또프로그램 재실행")
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨확인")
    print("4. 로또리스트 모두 확인")
    print("0. 프로그램 종료")
    print("-"*30)
    try:
        choice = int(input("원하는 번호 입력>> "))
        if choice == 1:
            mix_lotto()
        elif choice == 2:
            count = 0
            lotto2 = [i+1 for i in range(45)]
            while True:
                print(" [로또번호입력]")
                print("-"*50)
                for i in range(45):
                    if i%7==0: print()
                    print(lotto2[i],end="\t")
                print()
                if count == 6:
                    print(f" {count}번 입력 완료")
                    break
                choice = int(input("원하는 번호 입력(0. 취소)>> "))
                if choice == 0: break
                if choice<0 or choice> 45 :
                    print("다시입력")
                temp =0
                for i in lotto2:
                    if i == choice:
                        lotto2[i-1]="X"
                        my_lotto[count]=choice
                        count+=1
                        temp = 1
                if temp == 0:
                    print(f"{choice}는 해당 안됨 ")
                        
        elif choice == 3:
            print("[로또번호 당첨확인 ]")
            print("-"*50)
            for i in lotto[:6]:
                for j in my_lotto:
                    if i==j:
                        win_lotto.append(i)
            print("로또당첨번호 : ",lotto[:6] )
            print(f"내가 입력한 번호 : {my_lotto}")
            print(f"당첨된 로또번호 : {win_lotto}")
            print("당첨개수 : ",len(win_lotto))
        elif choice == 4:
            print("[로또리스트 모두 확인 ]")
            print("-"*50)
            print(my_lotto.sort())
        elif choice == 0:
            print("[프로그램 종료]")
            break
    except:
        print("잘못 입력하셨습니다. 다시 입력하세요.")
        continue
