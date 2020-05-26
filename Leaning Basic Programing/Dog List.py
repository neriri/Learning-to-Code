dogNames = []
while True:
    print('Enter the name of Dog ' + str(len(dogNames) + 1) + ' or Type "ok" to stop. :')
    dog = input()
    if dog =='ok':
        break
    dogNames = dogNames + [dog]
print('The dog names are:')
for dog in dogNames:
    print('  '+dog)
