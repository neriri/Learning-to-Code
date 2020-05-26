import pickle

waifuBook = {1:'Mei',2:'Misuzu',3:'Kurumi'}

pickle_open = open('dict.pickle','wb')
pickle.dump(waifuBook,pickle_open)
pickle_open.close()
