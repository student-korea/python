# with 함수 사용시f.close() 생략
# 모든 학생 영어 +2점하기
# with open("py0404/stu.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

# students = [
#     {"no":1,"name":"Eric","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
#     {"no":2,"name":"Hina","kor":70,"eng":90,"math":90,"total":250,"avg":83.33,"rank":3},
#     {"no":3,"name":"Casper","kor":100,"eng":90,"math":80,"total":270,"avg":90,"rank":2},
# ]

# f= open("py0404/stu.txt","r",encoding="utf-8")
# while True:
#     line = f.readline()
#     if not line:break
#     a_list = line.strip().split(",")

# print(a_list)

# print(int(a_list[3])+2)

# stu.txt ->영어 성적을 +1 증가하고 합계도 +1증가해서 출력
# 전체 리스트 출력

a_list=[0]*3
f= open("py0404/stu.txt","r",encoding="utf-8")
while True:
    for i in range(3):
        line = f.readline()
        a_list[i] = line.strip().split(",")
        a_list[i][3] = (int(a_list[i][3])+1)
        a_list[i][5] = int(a_list[i][2])+int(a_list[i][3])+int(a_list[i][4])
        a_list[i][6] = int(a_list[i][5])/3
        print(f"[{a_list[i][0]}, {a_list[i][1]}, {a_list[i][2]}, {a_list[i][3]}, {a_list[i][4]}, {a_list[i][5]}, {a_list[i][6]:.2f} , {a_list[i][7]}]")
    break


    


        
        
    