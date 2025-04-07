class Student:
    # no = 1
    # name = ""
    count = 1
    def __init__(self,name,kor,eng,math):
        self.no=Student.count
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg= self.total/3
        self.rank = 0
        Student.count+=1
        
    def __str__(self):
        return f"""{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"""
    
class Students:
    def __init__(self):
        self.students = []
        
    def add(self,s):
        self.students.append(s)
        
    def __str__(self):
        for s in self.students:
            print(s.no,s.name,s.ko,s.eng,s.math,s.total,s.avg,s.rank)
ss = Students()
s = Student("Eric",100,100,100)
s2 = Student("Hina",90,90,89)
s3 = Student("Rei",80,78,92)
ss.add(s)
ss.add(s2)
ss.add(s3)

print(s)

# class Student:
#     # no = 1
#     # name = ""
#     count = 1
#     def __init__(self,name,kor,eng,math):
#         self.no=Student.count
#         self.name = name
#         self.kor = kor
#         self.eng = eng
#         self.math = math
#         self.total = kor+eng+math
#         self.avg= self.total/3
#         self.rank = 0
#         Student.count+=1
    
# s = Student("Eric",100,100,100)
# print(s.no,s.name,s.kor,s.eng,s.math,Student.count)

# s2 = Student("Hina",99,99,98)
# print(s2.no,s2.name,s2.kor,s2.eng,s2.math,Student.count)
# print(s.no,s.name,s.kor,s.eng,s.math,Student.count)
# s3 = Student("Rei",90,90,89)
# print(s3.no,s3.name,s3.kor,s3.eng,s3.math,Student.count)
    
# s = Student()
# s.name = "Eric"
# print(s.no,s.name)



