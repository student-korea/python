# 이름입력 , 국어,영어 수학 입력

# a= input("이름을 입력하세요.")
# b= int(input("국어 점수를 입력하세요. "))
# c= int(input("수학 점수를 입력하세요. "))
# d= int(input("영어 점수를 입력하세요. "))
# e= int(input("과학 점수를 입력하세요. "))

# print("이름: ",a)
# print("합계: ",b+c+d+e)
# print("평균:  %.1f" %((b+c+d+e)/4))

#\n 엔터 \t tab
print("hello. \n nice to meet you.\t my name is karl")

# format(),f함수
# format() 문자 형태 함수
a=10
b=3
print("%d / %d = %2.f" % (a,b,a/b))
str_print="{} + {} = {:.2f}".format(a,b,a/b)
str_print2=f"{a} / {b} = {(a/b):.2f}"
print(str_print)
print(str_print2)