# def cal():
#     kor = int(input("number "))
#     eng = int(input("number2 "))
#     math = int(input("number3 "))
#     print(kor+eng+math)
#     print((kor+eng+math)/3)
    
# cal()

# def swap(num1,num2):
#     temp = num1
#     num1=num2
#     num2=temp
#     return num1,num2
# def add():
#     sum = 0
#     temp = 0
#     num1 = int(input("number "))
#     num2 = int(input("number2 "))
#     if num1>num2:
#         num1,num2 = swap(num1,num2)
#     for i in range(num1,num2+1):
#         sum = sum+i
#     print(f"{num1}부터 {num2}까지의 합 : {sum}")
    
# add()

# def cal():
#     list=[0]*5
#     sum = 0
#     for i in range(5):
#         list.append(int(input("number ")))
#         if list[i]%2==0:
#             sum +=list[i]
#     return sum

# print("짝수의 합 :",cal())

# def square():
#     x = int(input("number "))
#     y = int(input("number2 "))
#     return x*y*2,(x+y)*2

# a,b=square()
# print(f"사각형의 둘레 {b}, 넓이 {a}")

# def cal(x,y,z):
#     return x+y+z,(z+y+z)/3

# name = input("이름을 입력하세요. ")
# kor = int (input("국어 점수를 입력하세요. "))
# eng = int (input("영어 점수를 입력하세요. "))
# math = int (input("수학점수를 입력하세요. "))
# total,avg = cal(kor,eng,math)
# print(f"{name}의 국어: {kor} 영어 :{eng} 수학: {math} 합계 : {total} 평균: {avg:.2f}")
# students = [
#     {"no":1,"name":"Eric","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
#     {"no":2,"name":"Hina","kor":70,"eng":90,"math":90,"total":250,"avg":83.33,"rank":2},
#     {"no":3,"name":"Nicky","kor":60,"eng":100,"math":60,"total":220,"avg":73.33,"rank":3},
# ]

# def cal(s):
#     s['kor'] = int(input("수정할 국어점수를 입력하세요.>>"))
#     s['total'] = s['kor'] + s['eng'] + s['math']
#     s['avg'] = s['total']/3
    
# s = {"no":2,"name":"Hina","kor":70,"eng":90,"math":90,"total":250,"avg":83.33,"rank":2}
  

# cal(s)
# print("수정된 국어 점수:",s['kor'])    
# def stu_print():
#     for s in students:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        
# print("1.입력")
# print("2.출력")
# choice=int(input("원하는 번호를 입력하세요. "))
# if choice == 2:
#     stu_print()

# def  cal():
#     a=100 #함수내 일반 변수는 사라짐 bool in float str
#     b=200
#     return a,b
# # 함수밖
# a=10
# b=20
# print("함수호출전 a,b : ",a,b)

# cal()
# print("함수호출 후 a,b:",cal())

# def cal(a_list):
#     a_list[0] = 100
#     a_list[1] = 120
    

# a_list = [0,0]#리스트 타입 변수 : 주소값
# a_list[0] = 10
# a_list[1] = 20
# print("함수 호출 전 a_list :", a_list[0],a_list[1] )

# cal(a_list)
# print("함수 호출 후 a_list :", a_list[0],a_list[1] )

# def func1():
#     global a
#     a= 20
# a = 10
# print("a : ",a)
# func1()
# print("a : ",a)

# def cal(n1,n2):
#     return n1+n2

# def cal(n1,n2,n3):
#     return n1+n2+n3

# def cal(n1,n2,n3,n4):
#     return n1+n2+n3+n4

# n1 = 10
# n2 = 20
# n3 = 30
# n4 = 40
# result = cal(n1,n2)
# print(result)

# result2 = cal(n1,n2,n3)
# print(result)

# result3 = cal(n1,n2,n3,n4)
# print(result)

#가변 매개변수
# def cal (*num):
#     result = 0
#     for n in num:
#         result +=n
#     return result

# print("2개 합계 : ",cal(1,2))
# print("3개 합계 : ",cal(10,20,30))
# print("4개 합계 : ",cal(20,40,60,80))

# print()함수는 매개변수가 가변매개변수임

# 키워드 매개변수 -키워드 변수는 무조건 마지막에 있어야함.
# def cal(b,a=10):
#     return a+b

# print(cal(1))

def cal(*a,b=10): # 가매변수 키워드 변수 같이사용 시 팁
    result = b
    for i in a:
        result +=i 
    return result
print(cal(1,2,3,4,5,b=11))    