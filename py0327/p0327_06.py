# 
# num =7
# if 10>=num>=0:
#     print("'10에 해당되는 숫자입니다.")

# 3,4,5

num = int(input("number "))
while(num>12 or num <1):
    num = int(input("retry number "))
if 5>=num>=3: print("Spring")
elif 6<=num<=8: print("Summer")
elif 9<=num<=11: print("autumn")
else : print("winter")