f= open('py0404/a.jpg',"rb")
fdata = f.read()
f.close
print("파일 읽기완료")

# 폴더 존재 확인 : os.ppath.exists()
# 폴더 생성 : os.makedirs()
import os
if not os.path.exists("c:down1"):
    pass

ff= open('C:/down/b.jpg',"wb")
len = ff.write(fdata)
ff.close()

print("파일 저장완료")