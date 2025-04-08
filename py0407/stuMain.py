from stuModule import Student,Students
from stuFunc import *

while True:
    choice = tmenu_print()
    if choice == 1:
        stu_input()
    elif choice == 2:
        print("[학생성적 출력]")
        print('-'*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print('-'*60)
        for s in students.students:
            print(f"{s.no}\t{s.name}\t{s.kor}\t{s.eng}\t{s.math}\t{s.total}\t{s.avg:.2f}\t{s.rank}\t")
            
    # elif choice == 3:
    #     stu_adjust(students) #수정
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

    