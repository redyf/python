#Make a password generator
import random
# define the password length
length = int(input("How long do you want your password to be? "))
# define the password characters
characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# define the password
password = ""
# loop through the password length
for x in range(length):
    password += random.choice(characters)
# print the password
print(password)
# end of program