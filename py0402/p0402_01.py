i_list = [1,2,3,4,5,1,2,10]
dic = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100, "total":300}
print(dic)
txt_list = ['안녕','반가워','다음','내일','봐','잘','지내','봐요']

# #추가
# dic['kor'] = 100
# print(dic)

# i_list.append(100)
# print(i_list)

# #삭제
# del dic["no"]
# print(dic)

# del i_list[0]
# print(i_list)

# #수정
# dic['name'] = "Eric"
# print(dic)

# i_list[0] = 100
# print(i_list)

# #개별 출력
# print(dic["name"])
# #print(dic['kor']) error
# print(dic.get('kor')) #없을시 None 출력

# print(list[0])

# #딕셔너리 key value 출력
# print(dic.keys())
# print(dic.values())
# print(dic.items())

# if 'no' in dic:
#     print("O")
# else:
#     print("X")

# #정렬 
# import operator
# dic_sort = sorted(dic.items(),key=operator.itemgetter(0))
# print(dic_sort)

# i_list.sort()
# print(i_list)
# i_list.sort(reverse=True)
# print(i_list)

# for k in dic:
#     print(dic[k])

# for k,v in dic.items():
#     print(k,v)
    
# for i in i_list:
#     print(i)

# #1~10까지의 리스트 생성
# a_list = [i+1 for i in range(10)]
# print(a_list)

# b_list = [0]*10
# print(b_list)

# c_list = [i for i in range(1,51) if i %2==1] 
# print(c_list)

# # zip
# for i,t in zip(i_list,txt_list):
#     print(i,t)
    
# new_list = list(zip(i_list,txt_list))
# print(new_list)

# new_dic = dict(zip(i_list,txt_list))
# print(new_list)

new_list = i_list #얕은 복사
new_list2 = [*i_list] # 깊은 복사