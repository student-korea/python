import random
bin = int(input("몇 빙고? "))
num2 = int(input("몇 * 몇? "))
sample_list=[i+1 for i in range(num2*num2)]
random.shuffle(sample_list)
a_list = [[0]*num2 for i in range(num2)]
for i in range(num2):
    for j in range(num2):
        a_list[i][j]=sample_list[num2*i+j]
count = 0
discount = 0
bingo = 0
while True:
    for i in range(num2): #세로
        for j in range(num2):
            if a_list[count][i] == "$": discount +=1
            if a_list[count][i] == "X" or a_list[count][i] == "$":
                count +=1
            if discount == num2: count -=1
            if count == num2:
                for k in range(num2):
                    a_list[k][i] = "$"
                bingo +=1
                break
        discount = 0
        count = 0
    for i in range(num2): # 가로
        for j in range(num2):
            if a_list[i][count] == "$" : discount +=1
            if a_list[i][count] == "X" or a_list[i][count] == "$":
                count +=1
            if discount == num2: count -=1
            if count == num2:
                for k in range(num2):
                    a_list[i][k] = "$"
                bingo +=1
                break
        discount = 0
        count = 0
    for j in range(num2): # 왼대각선
        if a_list[count][count] == "$" : discount +=1
        if a_list[count][count] == "X" or a_list[count][count] == "$":
            count +=1
        if discount == num2: count -=1
        if count == num2:
            for k in range(num2): a_list[k][k] = "$"
            bingo +=1
            break
    discount = 0
    count = 0
    for j in range(num2): #오른대각선
        if a_list[count][(num2-1)-count] == "$": discount +=1
        if a_list[count][(num2-1)-count] == "X" or a_list[count][(num2-1)-count] == "$":
            count +=1
        if discount == num2: count -=1
        if count == num2:
            for k in range(num2): a_list[k][(num2-1)-k] = "$"
            bingo +=1
            break
    discount = 0
    count = 0
    print(" |",end=" ")
    for i in range(num2):
        print(f"{i}",end="\t")
    print()
    print("-"*40)
    for i in range(num2):
        print(f"{i}|",end=" ")
        for j in range(num2):
            print(f"{a_list[i][j]}",end="\t")
        print()
    if bingo==bin:
        print("!!!!!! 빙고 완성 축하드립니다. !!!!!!")
        break
    print()
    num = int(input(f"숫자를 입력하세요.(1~{num2*num2})>> "))
    while num > num2*num2 or num < 1 : num = int(input(f"다시 숫자를 입력하세요.(1~{num2*num2})>> "))
    stop = 0
    for i in range(num2):
        for j in range(num2):
            if a_list[i][j] == num:
                a_list[i][j] = "X"
                stop = 1
                break
        if stop == 1: break