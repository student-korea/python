# 파이썬 변수 타입
# - bool타입, 숫자 :int 타입, float타입 , str타입

#print()
print("hello")

#변수 선언
# a = 10
# num = 30

# print
# print("입력된 숫자 :" ,a)
# print("입력된 숫자 : %d" % (a))
# print("입력된 숫자 : {}".format(a))
# print(f"입력된 숫자 : {a}")

# 입력 - input -> str
# num1=int(input("숫자를 입력하세요."))
# num2=int(input("숫자를 입력하세요."))
# print(f"입력된 숫자 : {num1} {num2} / 합계 : {num1+num2}")

#학생성적 프로그램
# 이름 , 국어,영어 수학 입력 합계 평균 출력
print("-"*50)
print("학생 성적 프로그램")
name= input("이름을 입력하세요.")
kor= int(input("국어 점수를 입력하세요. "))
math= int(input("수학 점수를 입력하세요. "))
eng= int(input("영어 점수를 입력하세요. "))
print("-"*50)
print("이름\t국어\t수학\t영어\t합계\t평균")
print(f"{name}\t{kor}\t{math}\t{eng}\t{kor+math+eng}\t{((kor+math+eng)/3):.2f}")
print("-"*50)