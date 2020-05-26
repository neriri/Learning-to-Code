birthday = {'Alice': 'April 1', 'Bob':'July 3','Carol':'March 6'}

while True:
    print('Enter a name: (Input nothing to quit)')
    if name =='':
    name = input()
        break

    if name in birthday:
        print(birthday[name]+ ' is the birthday of ' +name)
    else:
        print('I do not have birthday information for ' +name)
        print('What is their birthday?')
        newbday= input()
        birthday[name] = newbday
        print('Birthday database updated.')

