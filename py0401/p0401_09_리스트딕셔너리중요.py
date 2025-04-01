# myset1={1,2,2,2,3,3,3,5,5,7,}
# print(myset1)

# menu_list = ['삼각김밥,바나나,삼각김밥','사과','바나나','도시락'.'신각김빔']
# print(set(menu_list))

# list = {1,2,3,4,5}
# #list2=['10,100','10,200','10,300','10,400','10,500']
# list2=["{:,d}".format((i+100)*100) for i in list]
# print(list2)

# n_list = [ i for i in range(1,51) if i% 3 ==0]
# print(n_list)

n_list = ['Eric','Hina','Casper','Sophia','Rei']
t_list = [100,99,89,79,199]
a_list = [100,99,89,79,199]


# zip() -> 2개의 리스트 합치기-> list type, dict type
print(list(zip(n_list,t_list,a_list))) # 수정 x 다수 가능
print(dict(zip(n_list,t_list))) # 수정 가능 2개만 가능(key ,value)
#tuple_list =list(zip(n_list,t_list))
# for n,t in zip(n_list,t_list):
#     print(f"{n}:{t}")

# students= {"no":1,"name":"Eric","kor":100}
# for key,value in students.items():
#     print(f"{key} : {value}")

# for key,value in enumerate(students):
#     print(f"{key} : {value}")
