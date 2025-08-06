import random
import string
length = int(input("Enter the password length: "))
letters = string.ascii_letters     
digits = string.digits              
symbols = string.punctuation        
all_chars = letters + digits + symbols
password = ''.join(random.choice(all_chars) for _ in range(length))
print("Random generated password is:", password)
