students = list()
student = []
while True:
    no = int (input("Number? "))
    name = input("What's your name? ")
    kor = int (input("korea score? "))
    eng = int (input("english score? "))
    math = int (input("math score? "))
    total = kor+eng+math
    avg = total/3
    rank=0

    student = [no,name,kor,eng,math,total,avg,rank]
    students.append(student)

# students=[
#     [1,'Eric',100,100,100,300,100.0,0],
#     [2,'Casper',100,100,100,300,100.0,0],
#     [3,'Hina',100,100,100,300,100.0,0]
# ]
# student=[1,'Eric',100,100,100,300,100.0,0]
    print("     [ 학생성적 프로그램 ]")
    print("-"*65)
    print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
    print("-"*65)
    for stu in students:
        for i,s in enumerate(stu):
            if i!=6: 
                print(s,end="\t")
            else:
                print(f"{s:.2f}",end="\t")
        print()