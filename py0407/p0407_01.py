#클래스의 형태 - 파일구성 : 다른 타입 형태를 넣을 수 있다는 장점

#변수 -> 배열(같은 타입) -> 다른 타입(구조체) -> 객체(클래스) - 변수 함수
# *객체 지향언어 - 고급언어
# - 변수에 대한 값을 확인,비교
# - 캡슐화 : 변수에 대한 직접 접근을 막을 수 있음.

# stu = [1,"Eric",100,100,100,300,100.0,1]
# while True:
#     stu[2] =300
#     print("1. 학생 출력")
    
#     choice = int(input("원하는 번호를 입력하세요.>> "))
#     if choice ==1:
#         print(stu)

#class 첫글자 대문자
class Stu:
    # 생성자 -클래스가 선언될 때 데이터를 받아서 변수에 저장 함수
    def __init__(self,no,name,kor,eng,math,total,avg,rank):
        self.no=no #class 안에 변수가 생성됨
        self.name=name
        if 0<kor<=100:
            self.kor=kor
        self.math=math
        self.__eng=eng
        self.total=total
        self.avg=avg
        self.rank=rank
        
s = Stu(1,"Eric",100,100,100,300,100.0,1)
s.eng
print(s.eng)        
# class Stu:
#     pass

# s = Stu() #클래스 선언
# s.no =1 # 변수 선언
# s.name = "Eric" #변수 선언
# s.korea =100 # 변수 선언

# print(s.no)