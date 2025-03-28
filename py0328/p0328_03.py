# for i in range(1,11):
#     print(i)

# a=10
# if a>5 and a<9:
#     print(a)
    
# a_list = [1,2,3,4,5]
# print(a_list[2])
# print(a_list[1:4]) # 시작위 치 : 끝나는 위치
# print(a_list[:3])
# print(a_list[::2])
# print(a_list[::3])
# print(a_list[::-1])# 역순
# print(a_list[:-1])

# a="hello"
# print(a[2])
# print(a[1:4])
# print(a[:3])
# print(a[2])
# print(a[::-1])
# print(a[:-1])

# print(a[:7])
# # print(a[7]) -error
# print(len(a_list))
# print(a_list[:len(a_list)-1])
# print(len(a))

# for i in range(1,11,2):
#     print(i,end=" ")
    
# sum =0
# for i in range(1,101):
#     sum = sum +i
# print(f"합계 {sum}")

# 합계가 100 넘는 위치는 언제일까요?

sum =0
for i in range(1,101):
    sum = sum +i
    if sum>=100:
        print(f"i : {i} \nsum : {sum} ")
        break
print(f"합계 : {sum}")