import random

dishwasher = ["Nerson", "Neriel", "Ernleen", "Patricia"]


decider = random.randint(0, len(dishwasher) - 1)
antispam = []
antispam.append(decider)
while True:
    decier = random.randint(0, len(dishwasher) - 1)
    while decider == antispam[-1]:
        decider = random.randint(0, len(dishwasher) - 1)
        if decider != antispam[-1]:
            break
    antispam.append(decider)
    #print(antispam)
    print('Choosen washer no['+str(len(antispam)-1)+']: '+ dishwasher[decider])
    tryagain = input("Decide who's the next? ")
    if input == "no":
        break
