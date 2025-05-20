from stuModule import Student,Students
from stuFunc import *

def sub_modify(choice,subject):
    print(f"[ {title[choice+1]}과목 수정]")
    print(f"현재 {title[choice+1]}점수 : {subject}")
    subject = int(input(f"수정할 {title[choice+1]}점수 입력 : "))  
    print(f"{subject} 점으로 {title[choice+1]}점수가 변경되었습니다.")
    return subject
           
def stu_total(self):
    self.total = self.kor +self.eng+self.math
def stu_avg(self):
    self.avg = self.total/3
while True:
    choice = tmenu_print()
    if choice == 1:
        stu_input()
    elif choice == 2:
        stu_output()
    elif choice == 3:
        print("[학생성적 수정]") #수정
        search = input("수정하고자 하는 학생 이름을 입력하세요.>> ")
        temp = 0 #찾지 못햇을 때 사용변수
        for s in students.students:
            if search == s.name:
                temp = 1
                print(f"{search} 학생을 찾았습니다. 성적을 수정합니다.")
                print("[ 수정과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 취소")
                try: choice = int(input("원하는 번호를 입력하세요.>> "))
                except Exception as e :print(e)
                if choice ==1: s.kor = sub_modify(choice,s.kor)
                elif choice ==2: s.eng = sub_modify(choice,s.eng)
                elif choice ==3: s.math = sub_modify(choice,s.math)
                else: break
                s.stu_total()
                s.stu_avg()
            if temp == 0:
                print(f"{search} 학생을 찾지 못했습니다. 다시 입력하세요.!! ")
                
                
    # elif choice == 4:
    #     stu_delete(students) #삭제
    # elif choice == 5:
    #     stu_array(students) #정렬
    # elif choice == 6:
    #     stu_search(students) #검색
    # elif choice == 7:
    #     stu_rank(students) #등수처리 
    # elif choice == 8:
    #     stu_save(students) #저장
    elif choice == 0:
        print(" [ 프로그램 종료 ]") #종료
        break

    