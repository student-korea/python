class Students:
    phone = "" #인스턴스 변수 - 각각의 객체별로 사용되는 변수
    address=""
    count =1 #클래스 변수 -공용 사용
    def __init__(self,name,kor,eng,math):
        self.no = Students.count #클래스 변수
        Students.count+=1
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor=eng+math
        self.avg =self.total/3
        self.rank = 0
    
    def s_total(self):
        self.total = self.kor+self.eng+self.math
        
    def s_avg(self):
        self.avg = self.total/3
    def s_print(self):
        print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
        
s = Students("Eric",100,100,100)
s.s_print()
s = Students("Hina",90,90,91)
s.s_print()
s3 = Students("Rei",80,80,88)
s3.s_print()

s.kor = 50
s.s_total()
s.s_avg()
s.s_print()