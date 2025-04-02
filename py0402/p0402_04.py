# def cal(x,y):
#     result = x+y
#     result2 = x-y
#     result3 = x*y
#     result4 = x/y
#     print(result)
#     print(result2)
#     print(result3)
#     print(result4)

# a,b=20,10
# c,d = 200,100
# e,f = 100,50

# cal(a,b)
# cal(c,d)
# cal(e,f)

# def add(x,y):
#     print(x)
#     print(y)
#     print(x+y)
    
# a= 10
# b=20
# c=30
# d=40

# add(a,b)
# add(a,c)
# add(a,d)
# add(c,d)
    
# print(" 누군가와")
# print("인사")

sum =0
def cal():
    global sum
    x = int(input("number "))
    y = int(input("number2 "))
    print("더하기 =",x+y)
    print("빼기 =",x-y)
    print("곱하기 =",x*y)
    print("나누기 =",x/y)
    sum += (x+y)
    return sum
    
cal()
cal()
cal()
print(sum)