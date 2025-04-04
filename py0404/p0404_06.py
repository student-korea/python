# students = [
#     {"no":1,"name":"Eric","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
#     {"no":2,"name":"Hina","kor":70,"eng":90,"math":90,"total":250,"avg":83.33,"rank":3},
#     {"no":3,"name":"Casper","kor":100,"eng":90,"math":80,"total":270,"avg":90,"rank":2},
# ]

# # 1. students 리스트를 문자열로 변환
# # 2. 파일쓰기해서 문자열로 저장
# f= open("py0404/stu.txt","w",encoding="utf-8")
# for s in students:
#     line = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
#     f.write(line)
# f.close

f= open("py0404/stu.txt","r",encoding="utf-8")
students =[]

f= open("py0404/stu.txt","r",encoding="utf-8")
while True:
    for i in range(3):
        line = f.readline()
        if not line: break
        s=line.strip().split(",")
        students.append({"no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])})
    break
f.close
for s in students:
    print(s)
