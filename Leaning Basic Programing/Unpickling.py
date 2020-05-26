import pickle
import requests

rawData = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')

print(rawData.text)
unpickled = pickle.load(rawData.text)

for x in unpickled:
    print(''.join([key * val for key, val in x ]))
