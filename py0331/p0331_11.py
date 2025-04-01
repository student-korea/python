import random
sample_list=[i+1 for i in range(25)]
random.shuffle(sample_list)
a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j]=sample_list[5*i+j]
count = 0
discount = 0
bingo = 0
while True:
    for i in range(5): #세로
        for j in range(5):
            if a_list[count][i] == "$": discount +=1
            if a_list[count][i] == "X" or a_list[count][i] == "$":
                count +=1
            if discount == 5: count -=1
            if count == 5:
                for k in range(5):
                    a_list[k][i] = "$"
                bingo +=1
                break
        discount = 0
        count = 0
    for i in range(5): # 가로
        for j in range(5):
            if a_list[i][count] == "$" : discount +=1
            if a_list[i][count] == "X" or a_list[i][count] == "$":
                count +=1
            if discount == 5: count -=1
            if count == 5:
                for k in range(5):
                    a_list[i][k] = "$"
                bingo +=1
                break
        discount = 0
        count = 0
    for j in range(5): # 왼대각선
        if a_list[count][count] == "$" : discount +=1
        if a_list[count][count] == "X" or a_list[count][count] == "$":
            count +=1
        if discount == 5: count -=1
        if count == 5:
            for k in range(5): a_list[k][k] = "$"
            bingo +=1
            break
    discount = 0
    count = 0
    for j in range(5): #오른대각선
        if a_list[count][4-count] == "$": discount +=1
        if a_list[count][4-count] == "X" or a_list[count][4-count] == "$":
            count +=1
        if discount == 5: count -=1
        if count == 5:
            for k in range(5): a_list[k][4-k] = "$"
            bingo +=1
            break
    discount = 0
    count = 0
    print(" |",end=" ")
    for i in range(5):
        print(f"{i}",end="\t")
    print()
    print("-"*40)
    for i in range(5):
        print(f"{i}|",end=" ")
        for j in range(5):
            print(f"{a_list[i][j]}",end="\t")
        print()
    if bingo==3:
        print("!!!!!! 빙고 완성 축하드립니다. !!!!!!")
        break
    print()
    num = int(input("숫자를 입력하세요.(1~25)>> "))
    while num > 25 or num < 1 : num = int(input("다시 숫자를 입력하세요.(1~25)>> "))
    stop = 0
    for i in range(5):
        for j in range(5):
            if a_list[i][j] == num:
                a_list[i][j] = "X"
                stop = 1
                break
        if stop == 1: break