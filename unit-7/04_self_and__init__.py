class Myclass:
    def __init__(self,xAxis,yAxis) -> None: #special method
        self.xAxis = xAxis
        self.yAxis = yAxis
        
obj1 = Myclass(10,20)
obj2 = Myclass(30,40)

print("For obj1 :",obj1.xAxis,obj1.yAxis)
print("For obj2 :",obj2.xAxis,obj2.yAxis)