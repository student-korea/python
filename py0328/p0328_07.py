# i = 0
# while i<10:
#     print(i)
#     i=i+1
    
# print("-"*50)
# for i in range(10):
#     print(i) 
    
# input_list = [1,5,10,9,8,20]

# a=5
# if a in input_list:
#     print(f"O {a} 존재함")
# else:
#     print(f"X {a} 존재안함")
def swap(a,b):
    t = a
    a = b
    b = t

list=[]
for i in range(10):
    po=int(input(f" {i+1}번째 number :"))
    while po in list: po=int(input("retry number :"))
    list.append(po)
n=1    
while n<9:
    for i in range(1,10):
        if list[i-1]>list[i]:
            swap(list[i-1],list[i])
print(list)
