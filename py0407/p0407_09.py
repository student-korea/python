class Stu:
    # no = 1
    # name = ""
    count = 1
    def __init__(self,no,name,kor,eng):
        self.no = no
        self.__name = name
        self.__kor = kor
        self.eng = eng
        
    def getName(self):
        return self.__name
    #Setter   
    def SetKor(self,kor):
        if 0<=kor<=100:
            self.__kor = kor 
        else:
            raise NotImplementedError("유효값 X")
        
    def getEng(self):
        return self.__eng
    #Setter   
    def SetEng(self,eng):
        if 0<=eng<=100:
            self.__eng = eng 
        else:
            raise NotImplementedError("유효값 X")    
    def __str__(self):
        return f"{self.no},{self.name},{self.__kor},{self.eng}"
      
s = Stu(1,"Eric",100)
s.__kor = 200
print(s.no,s.name,s.__kor)
print(s)

