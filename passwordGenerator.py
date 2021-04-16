import string
import random 

def passGen(a):
    random.seed()

    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    whitespace = " "

    password = ""

    for i in range(a):
        charType = random.randint(1, 4)
        if charType == 1:
            password += random.choice(letters)
        elif charType == 2:
            password += random.choice(digits)
        elif charType == 3:
            password += random.choice(punctuation)
        elif charType == 4:
            password += whitespace
    print(password)

passGen(10)       
