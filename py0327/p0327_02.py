#달러를 입력하면,원화 환산해서 출력
# 1-> 1467원 환산

# doller=int(input("달러를 입력하세요."))
# print(f"{doller:,d}$ -> {(doller*1467):,d}won")

# 1779원 동전으로 변환
# money=int(input("give money "))
# while(True):
#     ch500=money//500
#     money=money%500
#     ch100=money//100
#     money=money%100
#     ch50=money//50
#     money=money%50
#     ch10=money//10
#     money=money%10
#     print(f"500-{ch500},100-{ch100},50-{ch50},10-{ch10},1-{money}")
#     break

#원의 넚이 구하기

radius=int(input("give radius "))
print(f"radius : {radius} ,circumference : {(radius*2*3.14):0.2f}cm circle : {(radius**2*3.14):.2f}cm2")

# 사각형 넓이
row=int(input("give row "))
col=int(input("give column "))

print(f"row : {row} ,column : {col} , square perimeter : {(col+row)*2}cm square : {(row*col)}cm2")

# 사각형 넓이
row=int(input("give row "))
high=int(input("give high "))

print(f"row : {row} ,column : {high} , triangle : {((row*high)/2):.2f}cm2")
