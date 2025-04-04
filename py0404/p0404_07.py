f= open("py0404/stu.txt","r",encoding="utf8")
students=[]
while True:
    data=f.readline()
    if not data: break
    s=data.strip().split()
    students.append({"no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])})