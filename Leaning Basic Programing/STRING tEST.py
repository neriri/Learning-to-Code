tSreak = 'TTTTTTHTHT'
hSreak = 'HHHHHH'
coinList = ['TTTTTTHTHT','TTHTHHHTHT','HTHTTHHHHH','HTHTTHHHHH','HTHTTHHHHH']
findings = [x for x in coinList if tSreak in x]
print('Results are : ' + str(findings))




'''
if 'TTTTTTHTHT' in coinList:
        tSreak += 1
elif 'HHHHHH' in coinList:
        hSreak += 1
print('Streak for T: %s and H: %s'%(tSreak,hSreak))


if any('TTTTTT' in s for s in coinList):
    print('T Streak Detected')
elif any('HHHHHH' in s for s in coinList):
    print('H Streak Detected')'''
