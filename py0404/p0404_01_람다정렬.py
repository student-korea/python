def a(a,b):
    return a+b

print(a(10,20))

# def func(a,b,c):
#     return max(a,b,c)

# print(func(10,5,20)) 

#람다 lambda -> 함수 축약형
# def 함수명(매개변수) : return 값
# lambda 매개변수 : 리턴값  

# def func(x):
#     return x**2
# lambda a:a*20

# a_list=[1,2,3,4,5]
# aa_list=[]

# for i in a_list:
#     if i%2 ==0:
#         aa_list.append(i)
# print(aa_list)

# def func(x):
#     if x%2==0:
#         return x
    
# b_list = list(filter(func,a_list))
# print(b_list)

# c_lsit= list(filter(lambda x:x%2==0,a_list))
# print(c_lsit)

#map(함수,리스트)
# print(list(map(func,a_list)))

# print(list(map(lambda x:x**2),a_list))

students = [
    {"no":1,"name":"Eric","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":0},
    {"no":2,"name":"Hina","kor":70,"eng":90,"math":90,"total":250,"avg":83.33,"rank":0},
    {"no":3,"name":"Nicky","kor":60,"eng":100,"math":60,"total":220,"avg":73.33,"rank":0},
]

s_list = sorted(students,key=lambda x:x['name'])
print(s_list)
print("-"*60)
print(students)

print(students)
print("-"*60)
students.sort(key=lambda x:x['name'])
print(students)
print("-"*60)
students.sort(key=lambda x:x['name'],reverse=True)
print(students)
print("-"*60)
students.sort(key=lambda x:x['total'])
print(students)
students.sort(key=lambda x:x['total'],reverse=True)



#dict타입은 sort()함수를 사용할수 없음
# students.sort()
# print(students)

# #리스트 sort() 정렬됨.
# a_list = [20,50,10,40,90]
# a_list.sort()
# print(a_list)
# a_list.sort(reverse=True)
# print(a_list)
