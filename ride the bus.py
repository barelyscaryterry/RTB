import numpy as np
import termcolor as tc

rdeck = ['Ah','2h','3h','4h','5h','6h','7h','8h','9h','10h','Jh','Qh','Kh',
'Ad','2d','3d','4d','5d','6d','7d','8d','9d','10d','Jd','Qd','Kd']
blackdeck = ['Ac','2c','3c','4c','5c','6c','7c','8c','9c','10c','Jc','Qc','Kc',
'As','2s','3s','4s','5s','6s','7s','8s','9s','10s','Js','Qs','Ks']
deck = rdeck + blackdeck

def card_shown(x):
    if len(x) == 2 and x in rdeck:
        form1r =f" _____________ \n| { tc.colored(x,'red') }          |\n|             |\n|             |\n|             |\n|             |\n|          {tc.colored(x, 'red') } |\n|_____________|\n"
        result = form1r
    elif len(x) == 2 and x not in rdeck:
        form1b=f" _____________ \n| {x}          |\n|             |\n|             |\n|             |\n|             |\n|          {x} |\n|_____________|\n"
        result = form1b
    elif len(x) == 3 and x in rdeck:
        form2r = f" _____________ \n| { tc.colored(x,'red') }         |\n|             |\n|             |\n|             |\n|             |\n|         {tc.colored(x, 'red') } |\n|_____________|\n"
        result = form2r
    else:
        form2b = f" _____________ \n| {x}         |\n|             |\n|             |\n|             |\n|             |\n|         {x} |\n|_____________|\n"
        result = form2b
    return result

cardback = f" _____________ \n|             |\n|             |\n|             |\n|             |\n|             |\n|             |\n|_____________|\n"

playern = int(input('How many players are there? '))

def pl_cards(n):
    i = 1
    playerind = {}
    playernum = {}
    while i < n + 1 :
        name = input(f'Type name of player {i} then press ENTER :: ')
        playernum[i-1] = name
        playerind[playernum[i-1]] = list(np.random.choice(deck,4,replace=False))
        dARG = 0
        while dARG <= 3:
            deck.remove( playerind[ playernum[ i-1 ] ][dARG])
            dARG += 1
        i += 1
    return(playerind,playernum)

player_ind_num = pl_cards(playern)
playerind = player_ind_num[0]
playernum = player_ind_num[1]


pl_num_turnlist = list(range(playern) )
np.random.shuffle( pl_num_turnlist )

def isfat(cards,n):
    rdeck = ['Ah','2h','3h','4h','5h','6h','7h','8h','9h','10h','Jh','Qh','Kh','Ad','2d','3d','4d','5d','6d','7d','8d','9d','10d','Jd','Qd','Kd']
    x = cards[0]
    y = cards[1]
    z = cards[2]
    q = cards[3]
    card_list = [x,y,z,q]
    fatcounter = [] #makes binary list of cards (1 = len(3), 0 = len(2))
    for i in cards:
        if len(i) == 3:
            fatcounter.append(1)
        else:
            fatcounter.append(0)
    #blank card
    zerothflip = f" _____________     _____________     _____________     _____________ \n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    
    #first options = 2
    firstflip0000 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |             |   |             |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    firstflip1000 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |             |   |             |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    #second options = 4
    secondflip0000 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}           |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |          {y} |   |             |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    secondflip1000 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}           |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |          {y} |   |             |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    secondflip0100 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}          |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |         {y} |   |             |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    secondflip1100 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}          |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |         {y} |   |             |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    #third options = 8
    thirdflip0000 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}           |   |{z}           |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |          {y} |   |          {z} |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    thirdflip1000 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}           |   |{z}           |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |          {y} |   |          {z} |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    thirdflip0100 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}          |   |{z}           |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |         {y} |   |          {z} |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    thirdflip1100 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}          |   |{z}           |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |         {y} |   |          {z} |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    thirdflip0010 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}           |   |{z}          |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |          {y} |   |         {z} |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    thirdflip0110 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}          |   |{z}          |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |         {y} |   |          {z} |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    thirdflip1110 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}          |   |{z}          |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |         {y} |   |         {z} |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    thirdflip1010 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}           |   |{z}          |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |          {y} |   |         {z} |   |             |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    #fourth options = 16
    fourthflip0000 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}           |   |{z}           |   |{q}           |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |          {y} |   |          {z} |   |          {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip1000 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}           |   |{z}           |   |{q}           |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |          {y} |   |          {z} |   |          {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip0100 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}          |   |{z}           |   |{q}           |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |         {y} |   |          {z} |   |          {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip1100 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}          |   |{z}           |   |{q}           |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |         {y} |   |          {z} |   |          {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip0010 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}           |   |{z}          |   |{q}           |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |          {y} |   |         {z} |   |          {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip0110 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}          |   |{z}          |   |{q}           |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |         {y} |   |          {z} |   |          {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip1110 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}          |   |{z}          |   |{q}           |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |         {y} |   |         {z} |   |          {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip1010 =  f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}           |   |{z}          |   |{q}           |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |          {y} |   |         {z} |   |          {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n" 
   
    fourthflip0001 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}           |   |{z}           |   |{q}          |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |          {y} |   |          {z} |   |         {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip0011 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}           |   |{z}          |   |{q}          |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |          {y} |   |         {z} |   |         {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip0101 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}          |   |{z}           |   |{q}          |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |         {y} |   |          {z} |   |         {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip0111 = f" _____________     _____________     _____________     _____________ \n|{x}           |   |{y}          |   |{z}          |   |{q}          |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|          {x} |   |         {y} |   |         {z} |   |         {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip1001 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}           |   |{z}           |   |{q}          |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |          {y} |   |          {z} |   |         {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip1011 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}           |   |{z}          |   |{q}          |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |          {y} |   |         {z} |   |         {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip1101 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}          |   |{z}           |   |{q}          |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |         {y} |   |          {z} |   |         {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"
    fourthflip1111 = f" _____________     _____________     _____________     _____________ \n|{x}          |   |{y}          |   |{z}          |   |{q}          |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|             |   |             |   |             |   |             |\n|         {x} |   |         {y} |   |         {z} |   |         {q} |\n|_____________|   |_____________|   |_____________|   |_____________|\n"

    format = ''
    #formats for zeroth draw = 1
    if n == 0:
        format = zerothflip
    #formats for first draw = 2
    elif n == 1:
        if fatcounter[0] == 1:
            format = firstflip1000
        else:
            format = firstflip0000
    #formats for second draw = 4
    elif n == 2:
        if fatcounter[0] == 1:
            if fatcounter[1] == 1:
                format = secondflip1100
            else:
                format = secondflip1000
        elif fatcounter[1] == 1:
            format = secondflip0100
        else:
            format = secondflip0000
    #formats for 3 = 8
    elif n == 3:
        if fatcounter[0] == 1:
            if fatcounter[1] == 1:
                if fatcounter[2] == 1:
                    format = thirdflip1110
                else:
                    format = thirdflip1100
            else:
                if fatcounter[2] == 1:
                    format = thirdflip1010
                else:
                    format = thirdflip1000
        else:
            if fatcounter[1] == 1:
                if fatcounter[2] == 1:
                    format = thirdflip0110
                else:
                    format = thirdflip0100
            else:
                if fatcounter[2] == 1:
                    format = thirdflip0010
                else:
                    format = thirdflip0000
    #fourth options = 16
    else:
        if fatcounter[0] == 1:
            if fatcounter[1] == 1:
                if fatcounter[2] == 1:
                    if fatcounter[3] == 1:
                        format = fourthflip1111
                    else:
                        format = fourthflip1110
                else:
                    if fatcounter[3] == 1:
                        format = fourthflip1101
                    else:
                        format = fourthflip1100
            else:
                if fatcounter[2] == 1:
                    if fatcounter[3] == 1:
                        format = fourthflip1011
                    else:
                        format = fourthflip1010
                else:
                    if fatcounter[3] == 1:
                        format = fourthflip1001
                    else:
                        format = fourthflip1000
        else:
            if fatcounter[1] == 1:
                if fatcounter[2] == 1:
                    if fatcounter[3] == 1:
                        format = fourthflip0111
                    else:
                        format = fourthflip0110
                else:
                    if fatcounter[3] == 1:
                        format = fourthflip0101
                    else:
                        format = fourthflip0100
            else:
                if fatcounter[2] == 1:
                    if fatcounter[3] == 1:
                        format = fourthflip0011
                    else:
                        format = fourthflip0010
                else:
                    if fatcounter[3] == 1:
                        format = fourthflip0001
                    else:
                        format = fourthflip0000
   
    for i in card_list:
        if i in rdeck:
            format = format.replace(i,tc.colored(i,'red'))
    return format



def beforebus():
    ordinal = {1:"first", 2:"second",3:"third",4:"fourth"}
    m = 1
    while m <= 4:
        n = 0
        while n < playern:
            num_up_now = pl_num_turnlist[ n % playern ]
            name_up = playernum[ num_up_now ]
            playerdeck = playerind[ name_up ]
            print(f"{name_up}'s {ordinal[m]} turn ")
            print( isfat(playerdeck,m-1) )
            input(f'Press ENTER to flip your {ordinal[m]} card')
            print( isfat(playerdeck, m) )
            input('Press ENTER to continue')
            n += 1
        m += 1
    return True


eightcards = []
regex = []
while len(eightcards) <= 8:
    candidate = np.random.choice(deck,replace=False)
    if len(candidate) == 3 and candidate[0:2] not in regex:
        eightcards.append(candidate)
        regex.append(candidate[0:2])
    elif len(candidate) == 2 and candidate[0] not in regex:
        eightcards.append(candidate)
        regex.append(candidate[0])
    else:
        continue
fat1 = eightcards[0:4]
fat2 = eightcards[5:9]

def split(cards):
    suitless = []
    for i in cards:
        if len(i) == 3:
            suitless.append(i[0:2])
        else:
            suitless.append(i[0])
    return suitless


def afterbus():
    print( isfat(fat1,4) +  isfat(fat2,2 ))

afterbus()

































        
        









