# txt = "안녕하세요"
# a_list = [1,2,3,4,5]

# #문자열도 인덱스번호 가짐
# print(txt[1])
# print(a_list[1])

# print(a_list[1:3])
# print(txt[1:3])
# print(txt[2:])
# print(txt[:3])

# print(txt*3)
# print("-"*50)
# print(len(txt))

# print(txt[::-1])

# txt = "abBBcDd"
# print(txt.upper()) #대문자
# print(txt.lower()) #소문자
# print(txt.swapcase()) #대->소, 소->대
# print(txt.title()) #첫글자 대문자

#
# txt = "hello nice to meet you i am playing game "
# print(txt.count("nice"))
# print(txt.count("i"))
# print(txt.find("to"))
# print(txt.find("ro"))

# t = "aaa.py"
# print(t.endswitch("py")) #있으면 True, 없으면 False

# txt = " 안녕하 세요   "
# # print(txt)
# # print(txt.strip()) # 앞뒤공백제거 - rstrip(오른) , lstrip(왼)
# print(txt.replace(" ",""))
# print(txt.replace("안녕","Hello"))
# txt1 = "hello nice to meet you i am playing game "
# print(txt1.replace("hello","Hello"))

# txt2 = "----파이-썬 ---"
# print(txt2.strip("-"))
# print(txt2.replace("-",""))

# txt = "a,b,c,d,안녕,반가워"
# txt_list = txt.split(",")
# print(txt_list)

# txt="1/Eric/100/100/100/300/100/0.1"
# txt_list = txt.split("/")
# print(txt_list)
# txt_list[1] = 'Hina'
# print(txt_list) 

# txt = ","
# txt2=txt.join("Hello")
# print(txt2)

# score = ['100','99','90']
# def cal(x):
#     return int(x)*100
# s_list = list(map(cal,score))
# print(s_list)
# sum = 0
# for s in score:
#     sum = sum+int(s)
# print("합계 :",sum)

# a="1234"
# if a.isdigit():
#     print("숫자로 가능합니다.")

# my_input=input("num? ")
# if my_input.isdigit():
#     my_input= int(my_input)
# else :
#     print("Enter num ")

print('1234'.isdigit())
print('abc'.isalpha())
print('abc123'.isalnum())
print('abc'.islower())
print('ABC'.isupper())

    
    