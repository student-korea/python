import math
import random

a = 3.141592
b = 3.51582

# a에서 소수점 3자리에서 올림해서 2자리까지 표시
# print(math.ceil(a*100)/100)
# b에서 소수점 5자리에서 올림해서 4자리까지 표시
# print(math.ceil(b*10000)/10000)
# #올림
# print(math.ceil(a))
# #반올림
# print(round(b,3))
# print(round(a,4))
# #내림
# print(math.floor(b))
# print(dir(math))

# print(random.randint(1,45)) #1~45까지 랜덤

# a_list = [1,2,3,4,5]
# print(random.choice(a_list)) #리스트중 1나 선택

# print(random.sample(a_list,2)) # 리스트중 2개 선택

# print(random.sample(a_list,3))

# random.shuffle(a_list) #리스트 랜덤 셔플
# print(a_list)

# 카드모양 SPADE-4,DIAMOND-3,HEART-2,CLOVER-1
# 번호 1-A,2,3,4,5,6,7,8,9,10,11-J,12-Q,13-K
# 13개
# 카드 총 개수 :52장

# 리스트 딕셔너리
# cList = [
#     {"shape":"SPADE","no":1},{"shape":"SPADE","no":2}
# ]

import random
clist = []
sh = ["CLOVER","HEART","DIAMOND","SPADE"]
no = [" ","A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]

for i in range(52):
    clist.append({"shape":i//13,"no":i%13+1})

random.shuffle(clist)

myCard = []
youCard = []

# 카드 5
for i in range(5):
    myCard.append(clist[i])
    
for i in range(5,10):
    youCard.append(clist[i])
    
for i in myCard:
    print(f"[{sh[i['shape']]}, {no[i['no']]}]")
print()
for i in youCard:
    print(f"[{sh[i['shape']]}, {no[i['no']]}]")    

win_list=[]
lose_list=[]
draw_list=[]

score = [0]*5
for i in range(5):
    if myCard[i]['no'] > youCard[i]['no']: 
        score[i]+=2
    elif myCard[i]['no'] < youCard[i]['no']: 
        score[i]+=1
    else : 
        score[i]+=0

print(f"{score.count(2)},{score.count(1)},{score.count(0)}")
print("[ 승리카드 ]")
for i,c in enumerate(myCard):
    if score[i] == 2:
        print(f"[{sh[c['shape']]}, {no[c['no']]}]",end=", ") 
# for c in clist:
#     print(c['shape'],c['no'])
