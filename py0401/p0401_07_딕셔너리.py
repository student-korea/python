# number = [273,103,5,32,65,9,72,800,99]
# sum = 0
# for n in number:
#     if n>100:
#         sum+= n
#     else :
#         number.remove(n)
# print(sum)
# print(number)

# for n in number:
#     value = nlength = len(str(n))
#     print(f"자리수 : {length},값 : {value}")

dic1= {1:"a",2:"b",3:"c"}
print(dic1)

student1_list = [1,"홍길동",100]
student1 = {"no":1,"name":"Eric","kor":100}
print(student1)

stu =  {"학번":1000,"이름":"Eric","학과":'컴퓨터공학'}

#딕셔너리 추가
dic = {}
dic['no']=1
dic['name'] = name = input("What's your name? ")
dic['kor'] = 100
dic['kor'] = dic['kor']+dic['kor']
print(dic)

del dic['no'] #del 키를 입력하면 삭제
print(dic)

#수정
dic['name'] = 'Hina'
print(dic)
#print(dic['total']) #없는 키값 에러
print(dic.get('total')) # 없으면 None

print(dic.keys()) #key의 값을 리스트 형태로 출력
print(dic.values()) #values의 값을 리스트 형태로 출력
print(dic.items()) #튜플형태로 출력
for i,value in enumerate(dic):
    print(f"{i} : {value}")
    
for key in dic:
    print(key)
    print(dic[key])
    
if 'name' in dic:
    print(f"존재")
    
if 'no' in dic:
    print(f"no : {dic['no']}")
else:
    print("no 키")