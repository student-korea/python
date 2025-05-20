from stuModule import Student,Students

students=Students() #리스트 객체 선언
title =['번호','이름','국어','영어','수학','합계','평균','등수']

def tmenu_print():
    print(" "*20)
    print('[ 학생성적처리 프로그램]')
    print("-"*30)
    print("1.학생성적 입력")
    print("2.학생성적 출력")
    print("3.학생성적 수정")
    print("4.학생성적 삭제")
    print("5.학생성적 정렬")
    print("6.학생성적 검색")
    print("7.등수처리")
    print("8.학생성적 저장")
    print("0.프로그램 종료")
    print("*"*30)
    choice = 0
    try: 
        choice = int(input("원하는 번호를 입력하세요.>> "))
    except Exception as e :print(e)
    return choice

def stu_input():
        print("[학생성적 입력]")
        name = input(f"{Student.count} 이름 ")
        score = [0]*3
        for i in range(len(score)):
            score[i] = int(input(f"{title[i+2]}점수를 입력하세요.>>"))
        students.add(Student(name,*score))
        print(f"{name} 학생이 등록되었습니다.")
        print()

def stu_output():
    print("[학생성적 출력]")
    print('-'*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print('-'*60)
    for s in students.students:
        print(f"{s.no}\t{s.name}\t{s.kor}\t{s.eng}\t{s.math}\t{s.total}\t{s.avg:.2f}\t{s.rank}\t")  
        