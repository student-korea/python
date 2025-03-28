# 두 수를 입력받아, 두 수 사이의 합을 구하시오

# num1 = int(input("number1 "))
# num2 = int(input("number2 "))

# sum=0
# if num1>num2:
#     temp=num1
#     num1=num2
#     num2=temp
# for i in range(num1,num2+1) : sum = sum+i
    
# print(f"{num1}~{num2} 사이의 합 {sum}")

#구구단
num1 = int(input("number1 "))
num2 = int(input("number2 "))
if num1>num2:
    temp=num1
    num1=num2
    num2=temp
for i in range(num1,num2+1):
    print(f"[{i}단]")
    for n in range(1,10):
        print(f"{i}x{n} = {i*n}",end=" ")
    print()