import random
sample_list=[i+1 for i in range(25)]
random.shuffle(sample_list)
a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j]=sample_list[5*i+j]
print(a_list)
while True:
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
    num1 = int(input("X좌표를 입력하세요.>>"))
    if num1>4 or num1 <0: num1 = int(input("X좌표를 다시 입력하세요.>>"))
    num2 = int(input("Y좌표를 입력하세요.>>"))
    if num2>4 or num2 <0: num2 = int(input("Y좌표를 다시 입력하세요.>>"))
    a_list[num2][num1]= "X"
    
            
    