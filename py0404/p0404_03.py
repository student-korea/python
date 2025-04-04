# f= open("aa.txt","w",encoding="utf-8")
# f.write("안녕하세요\n")
# f.write("반가워요\n")
# f.close()

# f= open("aaa.txt","w",encoding="utf-8")
# for i in range(10):
#     f.write("안녕하세요.\n")
# f.close()

# f= open("py0404/memo.txt","w",encoding="utf-8")
# print("[ 메모장 ]")
# print("------------")
# print("저장하려는 글자를 입력하세요.(x. 종료)")
# while True:
#     line = input("")
#     if line.lower() == "x": break
#     f.write(line+"\n")
# f.close()

# w(다시쓰기)
# a(이어쓰기)

f= open("py0404/memo2.txt","w",encoding="utf-8")
f.write("1,Eric,100,100,100\n")
f.close

f= open("py0404/memo2.txt","a",encoding="utf-8")
f.write("2,Hina,90,90,80\n")
f.close