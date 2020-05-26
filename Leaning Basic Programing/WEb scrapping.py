import requests
import re


template = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
res = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=3875')

pattern = re.compile(r'nothing is (\d+)')

for i in range(400):
    search = pattern.finditer(res.text)
    if 'Divide' in res.text:
        clue = int(clue)/2
        print('Divide Crap')
    else:
        clue = ''
        for match in search:
            clue = clue +(match.group(1))
        
    link = template + str(clue)
    newRes = requests.get(link)
    res = newRes
    print(res.text)

print(link)
print('Job Done')

