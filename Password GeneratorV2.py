import random
total_letters = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L',
'm','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
total_symbols = ['!','@','#','$','%','^','&','*','(',')','-','+','=']
total_numbers = ['1','2','3','4','5','6','7','8','9','0']

print("Welcome to the super duper password generator!")
user_letters = int(input("Please enter how many letters you would like in your password\n"))
user_symbols = int(input("Please enter how many symbols you would like in your password\n"))
user_numbers = int(input("Please enter how many numbers you would like in your password\n"))

i, j, k = 0,0,0
final_password = []

for i in range(user_letters):
    random_integer_letters = random.randint(0,len(total_letters)-1)#51
    final_password.append(total_letters[random_integer_letters])
  
for j in range(user_symbols):
    random_integer_symbols = random.randint(0,len(total_symbols)-1)#12
    final_password.append(total_symbols[random_integer_symbols])

for k in range(user_numbers):
    random_integer_numbers = random.randint(0,len(total_numbers)-1)#9
    final_password.append(total_numbers[random_integer_numbers])

random.shuffle(final_password)
print("Your new password is: ")
print(*final_password, sep="")