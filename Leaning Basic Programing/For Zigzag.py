import sys, time

indent = 0
try:
    while True:
        if indent <20:
            for indent in range(0,21):
                print(' '*indent,end='')
                print('********')
                time.sleep(0.1)

        if indent >=0:
            for indent in range(20,0,-1):
                print(' '*indent,end='')
                print('********')
                time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit()
