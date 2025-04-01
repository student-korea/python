import random
# 1차원 리스트
s_list = [i for i in range(1,26)]
random.shuffle(s_list)

my_list = [[0]*5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        my_list[i][j] =s_list[5*i+j]
while True:
    print(" "*5,end="")
    print("[좌표맞추기 프로그램]")
    print("* |",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*42)
    for i in range(5):
        print(f"{i} |",end="\t")
        for j in range(5):
            print(my_list[i][j],end = "\t")
        print()
    print("-"*42)
    num = int(input("숫자를 입력하세요.>> "))
    for i in range(5):
        for j in range(5):
            if my_list[i][j] == num:
                my_list[i][j] = "X"
                break