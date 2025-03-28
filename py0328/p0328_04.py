#1 ~100 사이에 홀수만 더해 서 합계
sum = 0
for i in range(1,100,2): sum=sum+i
print(f"홀수 합계 : {sum}")

sum = 0
for i in range(1,101):
    if i%3==0 or i%7==0: sum=sum+i
        
print(f"3 또는 7의 배수 합계 : {sum}")
