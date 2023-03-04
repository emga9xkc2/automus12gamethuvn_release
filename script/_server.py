import random

listserver = []
for i in range(9):
    listserver.append((401, 302 + i * 25))


def getServer(server):
    if server == 18:
        server = 9
    return server

def phutRaBai():    
    phut = random.randint(30, 70)
    return 0