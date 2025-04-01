a_list = [1,2,3,4,5]

#삭제 명령어
del a_list[0] # index번호를 가지고 삭제
a_list.pop() #마지막 데이터 삭제
a_list.pop(2) #index번호 삭제
a_list.remove(2) #2라는 값을 삭제
a_list.clear() #모두 삭제

a_list.append(1)
a_list.append(2)
a_list.insert(0,"Eric") #d원하는 위치
a_list.extend([10,11,12]) #원하는 리스트 추가

a_list[0] = "Hina"
print(a_list)

for a in a_list:
    print(a)
    
a_list.append(['computer','software','music'])
print(a_list)

print(len(a_list)) # 리스트 길이

# 리스트 안에 해당 값 알기
s_list = [1,2,3,1,2,2,2,1,3,4,5,7,7,7,10,9,8]
print(f"{1} : {s_list.count(1)}")
num = 0
for s in s_list:
    if s == 1:
        num +=1

print(f"{1} : {num}")

#리스트 정렬
s_list.sort()
print(s_list)
# s_list.sort(reverse=True)
s_list.reverse()
print(s_list)