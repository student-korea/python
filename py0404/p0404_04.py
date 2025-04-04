# with
# with open("py0404/a1.txt","w",encoding="utf-8") as f:
#     f.write("안녕")
# print("저장")

#학생성적 파일 쓰기
f= open("py0404/stu.txt","a",encoding="utf-8")
count = 1
while True:
    no = count
    name = input(f"{no}번 이름을 입력하세요.(0.이전화면 이동)>> ")
    if name == '0': break
    kor = int (input("국어점수를 입력하세요. "))
    eng = int (input("영어점수를 입력하세요. "))
    math = int (input("수학점수를 입력하세요. "))
    total= kor+eng+math
    avg = total/3
    rank = 0
    lines = f"{no},{name},{kor},{eng},{math},{total},{avg:.2f},{rank}\n"
    count+=1
    f.write(lines)
f.close()
print("학생 성적이 저장되었습니다.")
