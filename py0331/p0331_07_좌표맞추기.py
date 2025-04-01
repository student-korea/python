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
    num = int(input("숫자를 입력하세요.>> "))
    stop = 0
    for i in range(5):
        for j in range(5):
            if a_list[i][j] == num:
                a_list[i][j] = "X"
                stop = 1
                break
        if stop == 1: break
    