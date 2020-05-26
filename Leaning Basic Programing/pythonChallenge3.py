import re
with open('pythonChallenge.txt', 'r') as x:
    source = x.read()
    pattern =re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
    search = pattern.finditer(source)
    for match in search:
        print(match.group(1),end='')

