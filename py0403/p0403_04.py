# 로또 프로그램
import random
# 6개 숫자 랜덤 번호 생성
# 6개 입력한 번호 생성
# 당첨번호 확인
# 출력
# 숫자맞추기 프로그램
lotto = [i+1 for i in range(45)]
lotto2 = [i+1 for i in range(45)]
my_lotto = [0]*6
win_lotto = []
def lotto_mix():
    global lotto
    random.shuffle(lotto)
print(lotto[0])
while True:
    lotto_mix()
    try:
        print("[ 로또 프로그램 ]")
        print("-"*30)
        print("1. 로또프로그램 재실행")
        print("2. 로또번호 입력")
        print("3. 로또번호 당첨확인")
        print("4. 로또리스트 모두 확인")
        print("0. 프로그램 종료")
        print("-"*30)
        choice = int(input("원하는 번호 입력>> "))
        if choice == 1:
            lotto_mix()
        elif choice == 2:
            count = 0
            lotto2 = [i+1 for i in range(45)]
            while True:
                print(" [로또번호입력]")
                print("-"*50)
                #로또 번호 순번출력
                for i in range(45):
                    if i%7 != 0 :print(lotto2[i],end ="\t")
                    else :
                        print()
                        print(lotto2[i],end="\t")
                print()
                if count >= 6:
                    print("로또번호 6개를 모두 입력하였습니다.! ")
                    break
                choice = int(input("원하는 번호 입력(0. 취소)>> "))
                if choice == 0 : break
                if choice <0 or choice>45:
                    print(f"{choice}번 번호는 없는 번호입니다. 다시 입력해 주세요. ")
                    continue
                temp = 0
                for i in lotto2:
                    if i == choice:
                        lotto2[i-1] = "X"
                        my_lotto[count] = choice
                        count +=1 
                        temp = 1
                if temp ==0:
                    print(f"{choice}번 번호는 해당되지 않는 번호입니다. 다시 입력하세요. ")
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
            print(" [로또리스트 모두 확인]")
            print("-"*50)
            print(my_lotto.sort())
        elif choice == 0:
            print(" [프로그램 종료]")
            print("-"*50)
    except:
        print("잘못 입력하셨습니다. 다시 입력하세요.")
        continue
