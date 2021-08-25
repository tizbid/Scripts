import string
from random import *

def password_generator(num =int(input("Enter any number greater than 9: "))):
    if num <= 8:
        num = int(input('Enter any number greater than 9: '))
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(8, num )))
    return password

if __name__ == '__main__':
    print(password_generator())
    