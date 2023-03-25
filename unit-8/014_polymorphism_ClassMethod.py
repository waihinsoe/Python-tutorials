#Polymorphism class method

class MgMg:
    def human(self):
        print("MgMg is a programmer.")
        print("MgMg is always coding")
class AgAg:
    def human(self):
        print("AgAg is a hacker.")
        print("AgAg is always learning")
class KoKo:
    def human(self):
        print("KoKO is a scientist.")
        print("KoKO is always testing.")
class People:
    def fun(self,obj):
        obj.human()
        
mgmg = MgMg()
agag = AgAg()
koko = KoKo()
people = People()

people.fun(agag)
myList = [mgmg, agag, koko]
for obj in myList:
    people.fun(obj)
