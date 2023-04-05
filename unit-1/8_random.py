# Random
import random  # 483 843e2 348e3 438 927e2
import secrets

# secureNumber = secrets.SystemRandom()
# myList = [19,55,23,77,74]
# x = 0
# for i in range(len(myList)):
#     for j in range(10):
#         num = secureNumber.randint(1,99)
#         if num == myList[x]:
#             print(num)
#     x +=1

# print(random.random()) work between 0.0 and 1.0 for floating point

# Randint => (low,height)
# print(random.randint(3,15))

# Randrange => (low,height,step)
# print(random.randrange(0,10,2))

# Random.choice
# humen = ['wai', 'hin', 'soe', 'myint', 'htike', 'aung']
# print("selected name", random.choice(humen))

# Random.sample
# name = ['wai', 'hin', 'soe', 'myint', 'htike', 'aung']
# print("selected names :", random.sample(name, 5))

# Random.seed()
# random.seed(9)
# print('Random number of seed() :',random.random())

# random.shuffle()
# random generate value from list,tuple, dict,set
# name = ['wai','hin','soe','myint','htike','aung']
# print("Before shuffle :",name)
# random.shuffle(name)
# print("After shuffle :",name)

# random.uniform() for floating point
# print('uniform',random.uniform(0.3,4.5))

# random.triangular() for floating point
# print('triangular',random.triangular(2.3,4.6,1.5))
