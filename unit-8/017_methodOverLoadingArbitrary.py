class Price:
    def payment(self, *args):
        data = 0
        count = 0
        for i in args:
            count += 1
            data += i
        print("There are {0} parameters passed".format(count))
        return data

obj = Price()

print(obj.payment(10,20))
print(obj.payment(10,20,30,40,50))