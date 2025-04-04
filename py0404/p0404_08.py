students = [
    {"no":1,"name":"Eric","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
    {"no":2,"name":"Hina","kor":70,"eng":90,"math":90,"total":250,"avg":83.33,"rank":2},
    {"no":3,"name":"Nicky","kor":60,"eng":100,"math":60,"total":220,"avg":73.33,"rank":4},
    {"no":4,"name":"Alice","kor":85,"eng":85,"math":70,"total":240,"avg":80,"rank":3},
    {"no":5,"name":"Rei","kor":60,"eng":70,"math":90,"total":220,"avg":73.33,"rank":4},
]

# stu.txt 파일의 문자를 읽어와서 리스트 타입으로 변경
# -----------
# 리스트타입을 -> stu.txt 에 저장
# 딕셔너리형태를 -> 데이터만 저장
s={"no":1,"name":"Eric","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1}
data = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}"
print(s)
print("-"*50)
print(data)

f= open("py0404/stu.txt","w",encoding="utf8")
for s in students:
    data = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
    f.write(data)
f.close()