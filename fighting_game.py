import random
print('hello,player! please choose a version of the game:')
print('1.human-human, 2.human-computer, 3.human-smart computer')

def menu(version):
    version = int(input())
    if version == 1:
        return hh()    #human human
    if version == 2:
        return hc() #human computer
    if version == 3:
        return hsc()  #human smart comp
    else:
        print('incorrect number, try again')
hp1 = 50
hp2 = 50
f=[
   [0,0,0,0,0,0,0,0,0,0],
   [1,1,1,1,1,1,1,1,1,1],
   [2,2,2,2,2,2,2,2,2,0],
   [3,3,3,3,3,3,3,3,0,0],
   [4,4,4,4,4,4,4,0,0,0],
   [5,5,5,5,5,5,0,0,0,0]
   [6,6,6,6,6,0,0,0,0,0],
   [7,7,7,7,0,0,0,0,0,0],
   [8,8,8,0,0,0,0,0,0,0],
   [9,9,0,0,0,0,0,0,0,0]]


def hit(i):  #i- picked force 
    random_number = random.randint(0,10)  #success of the hit
    force = f[int(i)][random_number]
    return force

def hh():
    print('choose names of player1 and player2')
    pl1 = input
    pl2 = input
    line = random.randint(1,2)
    if line == 1: #turn 
        print('first'+ pl1+',second'+pl2)
        while hp1 >= 0 or hp2 >= 0:
            print(pl1+'pick the force')
            f1 = int(input())
            hp2 -= hit(f1)  #hp of the enemy decrease
            print(pl2+'pick the force')
            f2 = int(input())
            hp1 -= hit(f2)
    else:
        print('first'+ pl2+',second'+pl1)
        while hp1 >= 0 or hp2 >= 0:
            print(pl2+'pick the force')
            f2 = int(input())
            hp1 -= hit(f2)  #hp of the enemy decrease
            print(pl1+'pick the force')
            f1 = int(input())
            hp2 -= hit(f1)
    if hp1 > hp2:
        print(pl1+'win with hp'+hp1)
    if hp2 > hp1:
        print(pl2+'win with hp'+hp2)
    else: 
        print('drawn game')

    
    def hc():
    print('choose names of player and comp')
    pl = input
    comp = input
    line = random.randint(1,2)
    if line == 1: #turn 
        print('first'+ pl+',second'+comp)
        while hp1 >= 0 or hp2 >= 0:
            print(pl+'pick the force')
            f1 = int(input())
            hp2 -= hit(f1)  #hp of the enemy decrease
            print(comp+'pick the force')
            f2 = random.randint(1,9)
            hp1 -= hit(f2)
    else:
        print('first'+ comp+',second'+pl)
        while hp1 >= 0 or hp2 >= 0:
            print(comp+'pick the force')
            f2 = random.randint(1,9)
            hp1 -= hit(f2)  #hp of the enemy decrease
            print(pl+'pick the force')
            f1 = int(input())
            hp2 -= hit(f1)
    if hp1 > hp2:
        print(pl+'win with hp'+hp1)
    if hp2 > hp1:
        print(comp+'win with hp'+hp2)
    else: 
        print('drawn game')





