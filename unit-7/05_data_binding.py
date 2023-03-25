
class Myclass:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y 
    def myInfo(self):
        print("From Info",self.x," : " ,self.y)

obj1 = Myclass("apple","orange")
print("from Init :",obj1.x,obj1.y )
obj1.myInfo()
        