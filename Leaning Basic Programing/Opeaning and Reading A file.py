with open('Syrup.jfif', 'rb') as anyLet:
    with open('HalfSpirit Canon.jfif', 'wb') as anyLet1:
        readLimit = 1
        axeImg = anyLet.read(readLimit)
        while len(axeImg) > 0:
            anyLet1.write(axeImg)
            axeImg = anyLet.read(readLimit)





















''' readAtm = 10
    dataContents = f.read(readAtm)
    while len(dataContents) > 0:
        print(dataContents,end='')
        dataContents = f.read(readAtm)'''
