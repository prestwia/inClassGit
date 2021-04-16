import string
import random 

def passGen(a):
    random.seed()

    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    password = ""

    for i in range(a):
        charType = random.randint(1, 3)
        if charType == 1:
            password += random.choice(letters)
        elif charType == 2:
            password += random.choice(digits)
        elif charType == 3:
            password += random.choice(punctuation)

        
