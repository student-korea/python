fruits=['사과','배','딸기','바나나','멜론']
for i in fruits:
    print(i)

for i,fruit in enumerate(fruits):
    print(f"{i+1}.{fruit}") 
    if len(fruit)-1 != 1:print(f"{i+1}.{fruit}",end="t")
    else: print(f"{i+1}.{fruit}",end=",")
        
           
# scores = [65,90,100,100,50]

# for score in scores:
#     print(score,end=",")