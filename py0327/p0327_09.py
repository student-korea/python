import random
# ran_num=random.randint(1,5) 
# in_num = int(input("random"))
# if ran_num == in_num:
#     print("O")
# else:
#     print("X")

# 1~100까지의 숫자 10개를 입력받음
num = []
# for i in range(1,11):
#     print(i,end=" ")
    
ran_num=random.randint(1,100)

for i in range(1,11):
    in_num = int(input("number: "))
    num.append(in_num)
    if ran_num==in_num:
        print(f"O 랜덤 숫자:{ran_num} 시도횟수: {i}")
        break
    else:
        print(f"x 입력 숫자:{in_num} 시도횟수: {i}")
        if ran_num > in_num:
            print("더 큰 수를 노리세요.")
        else :
            print("더 작은 수를 노리세요.")
            
print(f"입력된 숫자:{num}") 
print(f"랜덤 숫자:{ran_num}")