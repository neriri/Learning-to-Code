
a = 7
b = 8

def swapper(a,b):
    a =[a,b]
    b = a[0]
    a= a[1]
    print('The value of A: ' + str(a))
    print('The value of B: ' + str(b))
    return (a,b)
swapper(a,b)



