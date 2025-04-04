students =[
    {"no":1,"name":"Eric","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
    {"no":2,"name":"Hina","kor":70,"eng":90,"math":90,"total":250,"avg":83.33,"rank":3},
    {"no":3,"name":"Casper","kor":100,"eng":90,"math":80,"total":270,"avg":90,"rank":2}
]

print(max(students,key=lambda x:x['no'])['no']+1)
print(len(students))