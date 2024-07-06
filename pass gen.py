import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
len_letters = int(input("How many letters would you like in your password?"))
len_symbols = int(input("How many symbols would you like?"))
len_numbers = int(input("How many numbers would you like?"))

p=[]

for char in range(1,len_letters + 1):
   p.append(random.choice(letters))

for char in range(1,len_symbols + 1):
    p.append(random.choice(symbols))

for char in range(1,len_numbers + 1):
   p.append(random.choice(numbers))

random.shuffle(p)

password = ""
for char in p:
  password += char

print("The password is:",password)