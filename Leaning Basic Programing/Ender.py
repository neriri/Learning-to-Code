
someList = []
total = int(len(someList))
def ender(someList):
    if someList == []:
        print('Empty List')
    else:
        for i in  range(total -1):
            print((someList[i])+', ',end='')
        print('and '+ someList[-1])
ender(someList)

