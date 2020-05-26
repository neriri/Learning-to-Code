def division(devided):
    try:
        return 42 / devided
    except ZeroDivisionError:
        print('Error Invalid Divison')

print(division(2))
print(division(12))
print(division(0))
print(division(1))


