#예외 처리

#1. 구문 에러 - 오타
#2. 런타임 에러

print("데이터 출력")
a_list  = [1,2,3,4,5]
for a in a_list:
    print(a)
    
# for i in range(6):
#     print(a_list[i])
    
# -프로그램 종료

#예외 처리 방법 : if 조건문 ,예외처리
# print("1. 학생 성적 출력")

# choice = int(input("원하는 번호를 입력하세요.>> "))
# if choice.isdigit():
#     choice.int(choice)
# else: print("숫자만 입력이 가능")
# print("입력한 번호 : ",choice)

# 예외처리
print("1. 학생 성적 출력")
choice = int(input("원하는 번호를 입력하세요.>> "))
try :
    choice.int(choice)
except Exception as e: 
    print("숫자만 입력이 가능")
    print(e)
print("입력한 번호 : ",choice)