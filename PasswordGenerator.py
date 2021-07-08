import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','{','}','(',')','[',']','+','-','/']
print("Welcome To Password Generator!")
p_letters = int(input("How many letters you want in your password?\n"))
p_numbers = int(input("How many numbers you want in your password?\n"))
p_symbols = int(input("How many symbols you want in your password?\n"))

"""
password = ""
for char in range(1, p_letters+1):
    password += random.choice(letters)
for num in range(1, p_numbers+1):
    password += random.choice(numbers)
for sym in range(1, p_symbols+1):
    password += random.choice(symbols)
print("Password:", password)
""" 
password_list = []
for char in range(1, p_letters+1):
    password_list.append(random.choice(letters))
for num in range(1, p_numbers+1):
    password_list.append(random.choice(numbers))
for sym in range(1, p_symbols+1):
    password_list.append(random.choice(symbols))
print("Password:", password_list)
random.shuffle(password_list)
print("Shuffled Password:",password_list)
