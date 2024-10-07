import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
         't','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
         'Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','*','(',')','$','%','^']
number=['0','1','2','3','4','5','6','7','8','9']
print("Welcome to password generator!")
n_letters=int(input("Enter the number of letters:"))
n_symbols=int(input("Enter the number of symbols:"))
n_number=int(input("Enter the number of numbers:"))
password_list=[]
for x in range(1,n_letters+1):
    char=random.choice(letters)
    password_list+=char

for y in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list+=char
# print(password)
for z in range(1,n_number+1):
    char=random.choice(number)
    password_list+=char
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for  char in password_list:
  password+=char

print(password)

