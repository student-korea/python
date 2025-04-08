import time
import random
class Card:
    # self.shape
    # self.number
    #__str__
    def __init__(self,shape,number):
        self.shape=shape
        self.number=number

class CardFunc:
    def cardSuffles():
        pass
    def cardGive():
        pass
    def cardVictory():
        pass

#cardMain.py
#카드 리스트 호출
#카드 객체 호출
#각각 5장을 나눠준 다음, 비교해서 큰수가 승리하는 형태

shape = ["Clover","Heart","Diamond","Spade"]
number = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
deck = []
you_cardhand=[]
my_cardhand=[]

for i in range(4):
    for j in range(13):
        deck.append({"shape":shape[i],"number":number[j]})

random.shuffle(deck)
count =0
for s in deck:    
    if count%2==0:
        my_cardhand.append(s)
    else: you_cardhand.append(s)
    count +=1
    if count ==10:
        break
    
print(my_cardhand)
print(you_cardhand)
count = 0

for s in reversed(number):
    for i in my_cardhand:
        if isinstance(s, str):
            if s == f"{i['number']}":
                print(f"가장 큰 카드: {s}")
                count += 1
                break
        elif isinstance(s, int): 
            print(f"가장 큰 카드: {s}")
            count += 1
            break
    if count==1:
        break
                









# for s in deck:
#     print(s['shape'],s['number'])


# while True:
#     print("[카드 게임]")
#     print("카드를 셔플하겠습니다.")
#     print("샥")
#     time.sleep(2)
#     print("샥")
#     time.sleep(2)
#     print("샥")
#     time.sleep(2)
#     print("샥")
#     time.sleep(2)
    
    