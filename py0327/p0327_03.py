name = input("name ")
kor = int(input("korea "))
math = int(input("math "))
eng = int(input("english "))
print('-'*50)
print("               학생 성적 프로그램")
print('-'*50)
print("이름\t국어\t수학\t영어\t합계\t평균")
print(f"{name}\t{kor}\t{math}\t{eng}\t{kor+math+eng}\t{((kor+math+eng)/3):.2f}")


