#while 문
# i=0
# while i<10:
#     print(i)
#     i=i+1

# for문
# for i in range(10):
#     print(i)

# sum = 0
# for i in range(1,11):
#     a=int(input(f"number {i}: "))
#     sum = sum + a
# print(f"결과 = {sum}")

# sum = 0
# i=1
# while i<=10:
#      a=int(input(f"number {i}: "))
#      sum = sum +a
#      i=i+1
# print(f"결과 = {sum}")
#random.shuffle(list) 배열 내 섞기
#random.random() 0.00000000000<= x <1.0000000000
#int(random.random()*10)+1) # 1,10
# continue # 실행을 안하고 다시 처음으로

# 입력한 숫자합이 50을 넘기면 프로그램 종료하고 총합을 구하시오.(5의 배수는 제외)

# sum = 0
# while sum <=50:
#     a= int(input("숫자를 입력하세요: "))
#     if a%5 != 0: sum = sum+a
# print(f"총합은 {sum}입니다. 프로그램을 종료합니다.")
# 모양출력
# for i in range(10):
#     for j in range(i):
#         print("*",end = "")
#     print()

# a_list = [i+1 for i in range(100)]
# sum = 0
# for i in a_list:
#     sum = sum +i
#     if sum>200: 
#         sum = sum-i
#         print(f"위치값 : {i-1}",end=" ")
#         break
# print(f"합계 : {sum}")

# import random

# lotto = []
# my_input = []
# cor_input = []
# count = 0
# lotto = random.sample(range(1,45+1),6)
# for i in range(6):
#     a=int(input(f"number {i+1}: "))
#     while a in my_input or a<=0 or a>45 :
#         a=int(input(f"retry number {i+1}: "))
#     my_input.append(a)
#     if my_input[i] in lotto:
#         count=count+1
#         cor_input.append(a)
        
# print(f"로또 번호 : {lotto}")
# print(f"입력 번호 : {my_input}")
# print(f"맞춘 번호 : {cor_input}")
# print(f"맞춘 개수 : {count}")

# a_list = [1,2,3,4,5]
# print(a_list[5])

# a_list=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in range(3):
#     for j in range(3):
#         print(a_list[i][j],end ="\t")
#     print()

# a_list =[
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]
# ]
# for i in range(5):
#     for j in range(5):
#         print(f"{a_list[i][j]:2d}",end = " ")
#     print()

# # 1차원 리스트
# aa=[10,20,30]
# print(aa[0])

# #2차원 리스트
# aa = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ] 
# print(aa[:][:])

# 리스트 값 변경
# a_list = [1,2,3,4,5,6,7,8,9]
# a_list[5] = 10
# a_list[1:2] = [100,200]
# print(a_list)

# 역순 출력
# a_list = [1,2,3,4,5,6,7,8,9]
# print(a_list[::-1])

# import random
# #순차적 리스트 생성
# sample_list= [i+1 for i in range(25)]
# #리스트 섞기
# random.shuffle(sample_list)
# # 2차원 초기화 리스트 생성
# a_list = [[0]*5 for i in range(5)]
# #2차원 리스트에 랜덤 리스트 생성
# for i in range(5):
#     for j in range(5):
#         a_list[i][j] = sample_list[5*i+j]

# for i in range(5):
#     for j in range(5):
#         print(f"{a_list[i][j]:2d}", end=" ")
#     print()
    
# sample_list = [i+1 for i in range(25)]
# a_list = [[0]*5 for i in range(5)] # 초기화 

# for i in range(5):
#     for j in range(5):
#         a_list[i][j] = 5*i+(j+1)

# print(a_list)

sample_list = [[0]*5 for i in range(5)]
print(sample_list)

# sample_list = list()
# for i in range(5):
#     temp = []
#     for j in range(5):
#         temp.append(0)
#     sample_list.append(temp)
# print(sample_list)