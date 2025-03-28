# 3가지 조건
# 음수 , 0 ,양수

# b=int(input("give number "))
# if b==0: break
# elif b>0: print("양수")
# else: print("음수")

# b=int(input("give score "))
# if b>=60: print("합격")
# else: print("불합격")

# b=int(input("give score "))
# if b>=70: print("합격")
# elif b>=60: print("재시험")
# else:
#     print("불합격")

# pass 비울 때 씀         

b=int(input("give score "))
if b>=90:
    if b>96: print("A+")
    elif b>92: print("A")
    else: print("A-")
elif b>=80:
    if b>86: print("B+")
    elif b>82: print("B")
    else: print("B-")
elif b>=70:
    if b>76: print("C+")
    elif b>72: print("C")
    else: print("C-")
elif b>=60: 
    print("D")
    if b>66: print("+")
    elif b>62: pass
    else: print("-")
else:
    print("F")

    
# print("he",end="")
# print("llo")