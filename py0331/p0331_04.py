#1-25까지의ㅡ 랜덤 리스트를 생성 표적 게임
import random
#1차원 리스트 생성후 랜덤 섞기
sample_list = [i+1 for i in range(25)]
random.shuffle(sample_list)
#2차원 리스트 생성후 1차원 리스트 값을 넣기
a_list=[[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j] = sample_list[5*i+j]
ran = random.randint(1,26)
clear = 0
while True:
    print("         [좌표 맞추기 게임]       ")
    print(" |",end=" ")        
    for i in range(5):
        print(f"{i}",end="\t")
    print()
    print("-"*40)
    for i in range(5):
        print(f"{i}|",end =" ")
        for j in range(5):
            print(f"{a_list[i][j]}",end = "\t")
        print()
    print()
    if clear == 1:
        print("**축하합니다 클리어 했습니다.**")
        break
    num1 = int(input("X좌표를 입력하세요.>> "))
    while num1>4 or num1<0 : num1=int(input("다시 X좌표를 입력하세요.>> "))
    num2 = int(input("Y좌표를 입력하세요.>> "))
    while num2>4 or num2<0: num2=int(input("다시 Y좌표를 입력하세요.>> "))
    if a_list[num2][num1] == ran:
        clear = clear+1
        a_list[num2][num1] = "&"
        continue
    a_list[num2][num1] = "X"
