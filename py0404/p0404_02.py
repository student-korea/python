# 파일 열기 파일 읽기 -파일 쓰기 파일닫기
# 파일 열기 -3가지모드 : r:읽기 w:쓰기 a: 추가 b:이진파일 파일 복사
# f= open("a.txt","r")
# f= open("a.txt","w")
# f= open("a.txt","a")

#파일 읽기 - r 1줄 읽기
# f=open("a.txt","r",encoding="utf-8")
# print(type(f))
# for line in f:
#     print(line.strip())
# f.close()

# 파일 읽기- readlines(): 모두 읽기
# f=open("a.txt","r",encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line.strip())
    
# f.close

# f=open("C:/workspace/python/a.txt","r",encoding="utf-8")
 # f=open("/py0404/a.txt","r",encoding="utf-8") #폴더 안에 있는 파일 읽어오기
# for line in f:
#     print(line.strip())
# f.close

# while True:
#     line - f.readline()
#     if not line: break
#     print(line.strip())

f=open("py0404/news.txt","r",encoding="utf-8") #폴더 안에 있는 파일 읽어오기
for line in f:
    print(line.strip())
f.close