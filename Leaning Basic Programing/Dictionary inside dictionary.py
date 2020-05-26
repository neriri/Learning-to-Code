allWaifu ={'Plic': {'Loli': 5,'Ojou-sama':4,'Onee-san':6},
            '100 Kanojo':{'Loli':1, 'Tsundere':1,'Kuudere':2,'Onee-san':1},
            'Date ALive':{'Loli':2, 'Tsundere':2,'Imouto':2}}

def totalCharacter(waifu,numbers):
    waifuCounter = 0
    for kahit, ano in waifu.items():
        print('Ito yun Kahit: ' +kahit)
        #print('Ito yun Ano ' +str(ano))
        #print(waifuCounter)
        waifuCounter = waifuCounter + ano.get(numbers,0)
    return waifuCounter

print('Number of Characters Type:')
print('-Lolis ' + str(totalCharacter(allWaifu,'Loli')))
print('-Tsundere ' + str(totalCharacter(allWaifu,'Tsundere')))
print('-Ojou-sama ' + str(totalCharacter(allWaifu,'Ojou-sama')))
print('-Kuudere ' + str(totalCharacter(allWaifu,'Kuudere')))
print('-Onee-chan ' + str(totalCharacter(allWaifu,'Onee-san')))

