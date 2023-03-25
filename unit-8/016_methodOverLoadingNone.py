# MethodOverLoadingNone

class Price:
    def payment(self, x = None, y = None):
        if x != None and y != None:
            return x*y
        elif x != None:
            return x*x
        else:
            return None

obj = Price()
print(obj.payment(20,40))
print(obj.payment(10,20, 30,30))
    