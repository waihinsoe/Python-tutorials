class People:
    def __init__(self, id , age):
        self.id = id
        self.age = age
    def __add__(self, self1):
        data_id = self.id + self1.id
        data_age = self.age + self.age
        return data_id , data_age
    
p1 = People(101, 20)
p2 = People(123, 34)
p3 = People(223, 50)


total = p1 + p2
did, dage = total
p4 = People(did, dage)

finalTotal = p4 + p3
fId, fAge = finalTotal
result = fId + fAge
print(result)