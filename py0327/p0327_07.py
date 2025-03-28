#날짜 시간

import datetime #날짜 객체

now = datetime.datetime.now()
print(f"현재 시간 : {now} ")

print(f"현재 년 : {now.year} ")
print(f"현재 달 : {now.month} ")
print(f"현재 날 : {now.day} ")
print(f"현재 시 : {now.hour} ")
print(f"현재 분 : {now.minute} ")
print(f"현재 초 : {now.second} ")

# 시간이 12시 이상이면 오후 ,12시 미만이면 오전이라고 출력하세오
if now.hour >12:
    print(f"오후 {(now.hour-12):02d}:{now.minute:02d}")
else :
    print(f"오전 {now.hour:02d}:{now.minute:02d}")
    
print(f"{now.year}-{now.month:02d}-{now.day:02d}")