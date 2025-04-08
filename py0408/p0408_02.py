a = "홍길동님! 안녕하세요. 반갑습니다. 안녕 반가워. 안녕안녕"
count = 0
i = 0

while True:
    num = a[i:].find("안녕")
    if num != -1:
        count+=1
        i += num+1
    else: break
print(count)


# a = "홍길동님! 안녕하세요. 반갑습니다. 안녕 반가워. 안녕안녕"
# count = 0
# for i in range(len(a)):
#     if a[i] == "안":
#         if a[i+1] =="녕":
#             count +=1
            
# print(count)
# if "Hello" in a:
#     print("Hello is real")
# print(a.find("Hello"))