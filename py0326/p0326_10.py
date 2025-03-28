#숫자 2개를 입력받아 사칙연산 결과 값을 출력하시오.

a= int(input("숫자1 입력 "))
b= int(input("숫자2 입력 "))

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {(a/b):.1f}")

#이름입력 , 국어,영어 수학 입력

c= int(input("국어 점수를 입력하세요. "))
d= int(input("수학 점수를 입력하세요. "))
e= int(input("영어 점수를 입력하세요. "))

print(f"합계 : {c+d+e}")
print(f"평균 : {((c+d+e)/3):.2f}")