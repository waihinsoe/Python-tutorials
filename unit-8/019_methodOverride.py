# The class GrandChild inherits from the class Child, which inherits from the class Price
class Price:
    def payment(self):
        print("From parent")

class Child(Price):
    def payment(self):
        print("From child")
class GrandChild(Child):
    def payment(self):
        print("From GandChild")

    
obj = GrandChild()
obj1 = Price()
obj1.payment()
obj.payment()