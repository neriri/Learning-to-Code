import pprint
message = 'Please help me, I dont understand anyhing '
counter ={}

for characters in message:
    counter.setdefault(characters,0)
    counter[characters] = counter[characters] + 1

pprint.pprint(counter)


'''
def containsDuplicates(a):
    numList = {}
    for duplicate in a:
        numList.setdefault(duplicate, 0)
        numList[duplicate] = numList[duplicate] + 1 
    key = [k for (k, v) in numList.items() if v >= 2]
    return (key != [])

Lamda equivalent
containsDuplicates = lambda a: len(set(a)) != len(a)

'''