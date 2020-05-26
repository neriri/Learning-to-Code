
someList = ['Cloudy','Stormy','Rainy','Windy','Browny']

def ender(someList):
    total = int(len(someList))
    if someList == []:
        print('Empty List')
    else:
        for i in  range(total -1):
            print((someList[i])+', ',end='')
        print('and '+ someList[-1])
ender(someList)

