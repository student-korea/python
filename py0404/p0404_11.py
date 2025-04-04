import copy

# 예시 학생 데이터
students = [
    {'no': 1, 'name': '홍길동', 'kor': 90, 'eng': 85, 'math': 88, 'total': 263, 'avg': 87.67, 'rank': 1},
    {'no': 2, 'name': '김철수', 'kor': 80, 'eng': 75, 'math': 78, 'total': 233, 'avg': 77.67, 'rank': 2},
    {'no': 3, 'name': '이영희', 'kor': 85, 'eng': 90, 'math': 95, 'total': 270, 'avg': 90.00, 'rank': 1}
]

# 열 제목
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

# 학생 성적 정렬 함수
def sort_students(choice, students):
    students2 = copy.deepcopy(students)  # students를 깊은 복사하여 students2에 저장

    if choice == 1:  # 이름 순차정렬
        students2.sort(key=lambda x: x['name'])
    elif choice == 2:  # 이름 역순정렬
        students2.sort(key=lambda x: x['name'], reverse=True)
    elif choice == 3:  # 합계 순차정렬
        students2.sort(key=lambda x: x['total'])
    elif choice == 4:  # 합계 역순정렬
        students2.sort(key=lambda x: x['total'], reverse=True)
    elif choice == 5:  # 번호 순차정렬
        students2.sort(key=lambda x: x['no'])
    elif choice == 6:  # 번호 역순정렬
        students2.sort(key=lambda x: x['no'], reverse=True)

    return students2

# 출력 함수
def stu_output(students):
    print(" "*18, end="")
    print("[ 학생 성적 프로그램 ]")
    print("*"*60)
    print(f"{title[0]}\t{title[1]}\t{title[2]}\t{title[3]}\t{title[4]}\t{title[5]}\t{title[6]}\t{title[7]}")
    print("*"*60)
    for s in students:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()

# 학생 성적 정렬 옵션을 입력받고 정렬된 결과 출력
choice = int(input("정렬 기준을 선택하세요 (1: 이름 순차, 2: 이름 역순, 3: 합계 순차, 4: 합계 역순, 5: 번호 순차, 6: 번호 역순): "))
sorted_students = sort_students(choice, students)
stu_output(sorted_students)