class Price:
    def payment(self, dataType, *args):
        if dataType == "int":
            data = 0
            count = 0
            for i in args:
                count += 1
                data += i
            print("DataType is Integer.")
            print("There are {0} parameters passed".format(count))
            return data
        elif dataType == "str":
            data = ""
            count = 0
            for i in args:
                count += 1
                data += i
            print("DataType is String")
            print("There are {0} parameters passed".format(count))
            return data

obj = Price()

print(obj.payment("int",10,20))
print(obj.payment("int",10,20,30,40,50))
print(obj.payment("int",2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2))
print(obj.payment("str","Wai ","Hin ", "Soe")) 