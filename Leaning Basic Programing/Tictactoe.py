import random
tictacBoard = {'1':' ','2':' ','3':' ',
                '4':' ','5':' ','6':' ',
                '7':' ','8':' ','9':' '}

def displayBoard(board):
    print('═╦═╦═')
    print(board['1']+'║'+board['2']+'║'+board['3'])
    print('═╬═╬═')
    print(board['4']+'║'+board['5']+'║'+board['6'])
    print('═╬═╬═')
    print(board['7']+'║'+board['8']+'║'+board['9'])
    print('═╩═╩═')

turn = 'X'
for i in range(9):
    displayBoard(tictacBoard)
    print('Turn for '+turn+'.Move on which space?(1-9)')
    move = input()
    if move not in tictacBoard:
        announce =['Incorrect input: Nice, you Waste your TURN',\
        'Next player please...','Are you drunk!?...Next Player', \
        'Some people are stupid...Neexxtt!!', 'Follow the Instruction Please!',\
        'How about you read the instruction...hmm?~Nweexxth!']
        print(announce[random.randint(0,len(announce) - 1)])

    tictacBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    if 'X' in tictacBoard['1'] and 'X' in tictacBoard['4'] and 'X' in tictacBoard['7']or\
    'X' in tictacBoard['1'] and 'X' in tictacBoard['2'] and 'X' in tictacBoard['3']or\
    'X' in tictacBoard['3'] and 'X' in tictacBoard['6'] and 'X' in tictacBoard['9']or\
    'X' in tictacBoard['7'] and 'X' in tictacBoard['8'] and 'X' in tictacBoard['9']or\
    'X' in tictacBoard['7'] and 'X' in tictacBoard['5'] and 'X' in tictacBoard['3']or\
    'X' in tictacBoard['1'] and 'X' in tictacBoard['5'] and 'X' in tictacBoard['9']:
        print('Player with "X" Wins!')
        break
    elif 'O' in tictacBoard['1'] and 'O' in tictacBoard['4'] and 'O' in tictacBoard['7'] or\
    'O' in tictacBoard['1'] and 'O' in tictacBoard['2'] and 'O' in tictacBoard['3'] or\
    'O' in tictacBoard['3'] and 'O' in tictacBoard['6'] and 'O' in tictacBoard['9']or\
    'O' in tictacBoard['7'] and 'O' in tictacBoard['8'] and 'O' in tictacBoard['9']or\
    'O' in tictacBoard['7'] and 'O' in tictacBoard['5'] and 'O' in tictacBoard['3']or\
    'O' in tictacBoard['1'] and 'O' in tictacBoard['5'] and 'O' in tictacBoard['9']:
        print('Player with "0" Wins!')
        break
displayBoard(tictacBoard)
