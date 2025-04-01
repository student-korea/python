students = [
    {"no":1,"name":"Eric","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
    {"no":2,"name":"Hina","kor":70,"eng":90,"math":90,"total":250,"avg":83.33,"rank":3},
    {"no":3,"name":"Casper","kor":100,"eng":90,"math":80,"total":270,"avg":90,"rank":2},
]
count = 4
title =['번호','이름','국어','영어','수학','합계','평균','등수']
while True:
    print(" "*4,end="")
    print("[ 학생 성적 프로그램 ]")
    print("*"*30)
    print("1.학생성적 입력")
    print("2.학생성적 출력")
    print("3.학생성적 수정")
    print("4.학생성적 삭제")
    print("5.학생성적 정렬")
    print("6.학생성적 검색")
    print("7.등수처리")
    print("0.프로그램 종료")
    print("*"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))