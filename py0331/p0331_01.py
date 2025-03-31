a=10
a_list = [1,2,3,4,5]

print("a : ",a)

a_list[0] = 100
print("a_list ; ",a_list)

#깊은 복사
a_list = [1,2,3,4,5]
b_list=[*a_list]
b_list[1] = 100
print("b_list ; ",b_list)

b=a
b=1000
print("a : ",a)
print("b : ",b)
#주소값 얕은복사
b_list=a_list
print("a_list ; ",a_list)
# a_list = [1,2,3,4,5]
# sum=0
# for i in a_list:
#     sum=sum+i
# print(sum)

# for i in range(2,10):
#     print(f"{i}단")
#     for j in range(1,10):
#         print(f"{i} X {j} = {i*j:2d}",end=" ")
#     print()