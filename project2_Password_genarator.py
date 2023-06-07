import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A',
           'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','(','&',')','*','+','^']


print("Welcome to password genarator! ")

no_letter= int(input("Enter How many letters would you like in password:\n "))
no_symbol= int(input("Enter How many symbol would you like in password:\n "))
no_number= int(input("Enter How many number would you like in password:\n "))

password_list = []
for i in range(1, no_letter+1):
    char = random.choice(letters)
    password_list += char
for i in range(1, no_symbol+1):
    char = random.choice(symbols)
    password_list += char
for i in range(1, no_number+1):
    char = random.choice(numbers)
    password_list += char
print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(password)







