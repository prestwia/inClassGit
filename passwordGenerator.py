import string
import random 

def passGen(a):
    random.seed()

    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation


    charType = random.randint(1, 4)
    if charType == 1:
        print(random.choice(letters))
    elif charType == 2:
        print(random.choice(digits))
    elif charType == 3:
        print(random.choice(punctuation))


passGen(1)