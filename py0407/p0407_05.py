class Car:
    def __init__(self,color,tire,door): # 생성자
        self.color = color
        self.tire = tire
        self.door = door
    
    
    def speedUp(self,s):
        self.speed +=s
    def speedDownp(self,s):
        self.speed -=s

c=Car("red",4,5) #생성자 사용
c=Car("blue",5,5)

# a_list = [1,2,3,4,5]
# a_list = a_list
# a_list2=[*a_list]
 
# a = Car() #기본 형태
# a2 = Car()
# a3 = Car()

# a2.color ="blue"
# a2.tire = 5
# a2.door = 4

# a3.color = "black"
# a3.tire = 5
# a3.door = 5

    



