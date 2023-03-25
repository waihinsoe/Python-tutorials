import operator
from functools import reduce
print(operator.add(3,2))
print(operator.mul(3,2))
print(operator.truediv(3,2))
print(operator.floordiv(3,2))
print("#####################################333")

list = [1,2,3,4,5,6]

output1 = reduce(lambda x,y: x*y, list)
print("output from the reduce and lambda :", output1)

output2 = reduce(operator.mul, list)
print("output from the reduce and operator :",output2)

output3 = operator.lt(10,20)
output4 = operator.gt(10,20)
output5 = operator.is_("wai","hin")
output6 = operator.is_not("wai","hin")
output7 = operator.truth(list)
print(output3)
print(output4)
print(output5)
print(output6)
print(output7)
print(dir(operator))
