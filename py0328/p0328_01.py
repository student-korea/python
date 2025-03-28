# # 파이썬 변수 타입
# # - bool타입, 숫자 :int 타입, float타입 , str타입

# # bool type -True, False
# # int type -정수형
# # float type - 실수
# # str type - 문자열
# # if 10>3:
# #     print("true")

# # if True:
# #     print("true")
    
# # if False:
# #     print("false")
    
# # print(1+2)
# # print(1+1.2)

# # print("안녕",1)

# # print(f"{10/3:.2f}")

# # 숫자 타입변경 실수형->정수형 소수점 사라짐.
# print(int("1")+1)
# print(int(1.5))
# print(float("1.5"))
# print(str(1.5))

# a=10
# a=5
# b=1.5
# c="hello"

# print(c*a)

# list_a = [1,2,3,4]
# print(list_a)
# print(list_a[0]+list_a[1]+list_a[2]+list_a[3])

# score=input("데이터를 입력하세요")
# print("입력 데이터 : ",score)

# # 두 수를 입력받아 합계 평균을 출력하세요.
# num1=int(input("number1 "))
# num2=int(input("number2 "))
# print(f"합계: {num1+num2} 평균: {(num1+num2)/2} ")

# score=int(input("점수를 입력하세요"))
# if score>=60:
#     print("합격")
# else:
#     print("불합격")
    
# score=int(input("점수를 입력하세요"))
# if score>=70 : print("합격")
# elif score>=60 : print("재시험")
# else : print("불합격")

score=int(input("점수를 입력하세요 "))
if score>=90 : print("A")
elif score>=80 : print("B")
elif score>=70 : print("C")
elif score>=60 : print("D")
else : print("F")

    