message = [1,2,4,3,]

def duplicateFinder(message):
    counter ={}
    for characters in message:
        counter.setdefault(characters,0)
        counter[characters] += 1
    key = [k for (k, v) in counter.items() if  v != 1]
    print(message)
    print(key)
    return key

duplicateFinder(message)
