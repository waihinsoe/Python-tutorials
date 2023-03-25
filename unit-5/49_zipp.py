#Zip object

itr1 = [1,2,3,4,5]
itr2 = [10,20,30,40,50,60]

results = list(zip(itr1,itr2))
print(results)

for i in results:
    print(i)
    
for x in results:
    print(x)
    
print('#############################################')
###########################################################
#Filter
alphabet = ['a','b','c','d','e','f','i','o','u','j','k']

def VowelFilter (alphabet):
    vowel = ['a','e','i','o','u']
    if (alphabet in vowel):
        return True
    else:
        return False

filteredVowel = filter(VowelFilter , alphabet)

print(filteredVowel)

for i in filteredVowel:
    print(i)