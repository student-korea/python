a_list = [1,2,3,4,5]
del a_list[2]#특정 부분 삭제
print(a_list)

a_list.pop() #맨뒤 삭제
print(a_list)

a_list.remove(1) # 데이터값으로 삭제
print(a_list)

a_list.clear()#전체 삭제
print(a_list)



# a_list = [1,2,3]
# a_list.append(4)#마지막에 추가
# print(a_list)
# a_list.insert(1,100) #특정 위치에 값을 추가
# print(a_list)
# a_list.extend([100,200,300]) # 다른 리스트에 추가
# print(a_list)

# 리스트 내포
# a_list = [i for i in range(1,11)]
# print(a_list)

# 리스트 - append 추가방법
# a_list = []
# for i in range(1,11):
#     a_list.append(i)
    
# print(a_list)

# 인덱스 번호 사용하려면 enumerate
# a=[273,10,5,9,100,1000,50]
# for idx,value in enumerate (a):
#     print(f"{idx} : {value}")