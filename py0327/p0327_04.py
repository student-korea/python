# a = 10; b=11; 

# print(a==b)
# print(a!=b)
# print(a>b,a<b,a>=b,a<=b)
# a=int(input("give number "))
# if a<100:
#     print('true')
# else:
#     print("false")
while(True):
    b=int(input("give number "))
    if b==0:
        break
    if b>0:
        print("양수")
        if b%2==0:
            print("짝수")
        else:
            print("홀수")
    else:
        print("음수")
        if b%2==0:
            print("짝수")
        else:
            print("홀수")