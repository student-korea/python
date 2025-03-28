import random

#랜덤 1~45번까지의 숫자를 ran_list에 저장
#입력받은 숫자 6개를 my list 에 저장

ran_list = random.sample(range(1,45+1),6)
my_list=[]
co_list=[]
for i in range(6):
    my_input=int(input(f" {i+1} number :"))
    while my_input in my_list: my_input=int(input("retry number :"))
    my_list.append(my_input) 
n=0
count=0
while n<6:
    if my_list[n] in ran_list:
        co_list.append(my_list[n]) 
        count+=1
    n+=1
print(f"랜덤번호 {ran_list}")
print(f"입력번호 {my_list}")
print(f"당첨번호 {co_list}")
print(f"당첨횟수 : {count}")

# ran_input = random.randint(1,10)


# list=[]
# for i in range(10):
#     while ran_input in list: ran_input = random.randint(1,10)
#     list.append(ran_input)


# print(list)