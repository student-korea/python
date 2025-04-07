from sModule import Student,Students

students=Students()
title =['번호','이름','국어','영어','수학','합계','평균','등수']

def main_print():
    print(" "*20)
    print('[ 학생성적처리 프로그램]')
    print("-"*30)
    print("1.학생성적 입력")
    print("2.학생성적 출력")
    print("0.프로그램 종료")
    print("-"*30)
    try:
        choice = int(input("number "))
    except:
        print("Error")
    return choice
def stu_input():
    print("[학생성적 입력]")
    name = input("What's your name? ")
    score= [0]*3
    for i in range(len(score)):
        score[i] = int(input(f"What {title[i+2]} score ? "))
    students.add(Student(name,*score))
    print(f"{name} save")
    print()
def stu_output():
    print("[학생성적 출력]")
    print('-'*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print('-'*60)
    for s in students.students:
        print(f"{s.no}\t{s.name}\t{s.kor}\t{s.eng}\t{s.math}\t{s.total}\t{s.avg}\t{s.rank}")
