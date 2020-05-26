import re
emails = '''
nerielmadriaga12@gmail.com
miyazakilieren@yahoo.com
123blahblah@scam.phi
Doh.gov@ph-gov.org
watchtowerliblary@jw.org '''
domain = '''
https://www.google.com/
https://www.youtube.com/
http://kissanime.ru/
https://www.nasa.gov/
'''

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321222222
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

#pattern = re.compile(r'[\w.]+@[\w-]+\.\w+')
pattern = re.compile(r'https?://(www.)?(\w+.)([a-z]+)')
subbdomain = pattern.sub(r'\2\3',domain)
print(subbdomain)

#matches = pattern.finditer(domain)

#for match in matches:
    #print(match.group(2))

'''with open('Data.txt','r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)'''

