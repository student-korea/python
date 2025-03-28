# 숫자 맞추기 프로그램
import random

lotto = random.randint(1,45)

list = []
#----
for i in range(1,10):
    input_num = int(input(f"{i}번째 숫자를 입력하세요(1~45): "))
    list.append(input_num)
    if input_num==lotto:
        print("당첨")
        break
    elif lotto > input_num:
        print("멍청!"*i,f"{input_num} 보다 더 큰수를 입력하세요." )
    else:
        print("멍청!"*i,f"{input_num} 보다 더 작은수를 입력하세요." )

#---
    
print(f"랜덤번호 : {lotto}")
print(f"입력번호 : {list}") 