#CSPRNG
#Cryptographically Strong Pseudo-Random Number Generator
#secrets
import secrets
# print("Printing integer number using secrets module")
# SecureGenerator = secrets.SystemRandom()
# number_list = [1,2,3,5,22,66,45,36,67]
# RandomNumber = SecureGenerator.triangular(5.6,7.6,1.3)
# print('Secure Random number is :',RandomNumber)

print("Printing integer number using secrets module")
# print(secrets.token_bytes())
# print(secrets.token_hex(2)) #1 byte changes to 2 hex digits  

passwordResetLink = 'http://www.waihin.com/coder/reset='
passwordResetLink += secrets.token_urlsafe(32)
print('Secrets password reset is :',passwordResetLink)