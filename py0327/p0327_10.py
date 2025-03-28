#1~100까지 램덤숫자를  생성해서 정답을 맞추는 프로그램을 구축하시오.
#도전 횟수:
#도전 번호:
#랜덤 번호: 

import random
ran_num=random.randint(1,100)
num = []
n=0
for n in range(1,11):
    in_num=int(input("숫자를 입력하세요. "))
    num.append(in_num)
    if ran_num == in_num: break
    elif ran_num > in_num: print(f" X 입력번호:{in_num} 도전 횟수: {n} 더 크게")
    else : print(f" X 입력번호:{in_num} 도전 횟수: {n} 더 작게")
print("-"*50)        
print(f"도전 횟수 : {n}")
print(f"도전 번호 : {num}")
print(f"랜덤 번호 : {ran_num}")

#drama