import random

def randomThought(givenAnswer):
    if givenAnswer == 1:
        return 'You think I am crazy!?'
    elif givenAnswer == 2:
        return 'A sane man would run'
    elif givenAnswer == 3:
        return 'What ever lets start shooting'

print(randomThought(random.randint(1,3)))
