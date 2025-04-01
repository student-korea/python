# list = [1,2,3,11,2,3,5,6,8,9,10,1,2]
# #dic = {1:3,2:3,3:1,5:1,6:1,8:1,9:1,10:1,11:1}
# dic = {}

# for i in list:
#     if i not in dic: #존재 확인
#         dic[i]=0
#     #dic[i] = dic[i]+1 키 몇개존재 확인
#     dic[i] += dic[i]
# for i,d in enumerate(dic):
#     print(f"{i} : {dic[d]}")
# print(dic)

list=["gd","iu","aespa","twice","ive",
      "gd","ive","ive","iu","iu",
      "gd","gd","gd","iu","iu",
      "aespa","aespa","aespa","aespa","aespa",
      "twice","gd","twice","iu","twice",
      "ive","ive","ive","ive","ive"]

singer = {}
for i in list:
    if i not in singer:
        singer[i]=1
    singer[i]+=1
for i,s in enumerate(singer):
    print(f"{i} : {singer[s]}")
for i,s in singer.item():
     print(f"{i} : {singer[s]}")