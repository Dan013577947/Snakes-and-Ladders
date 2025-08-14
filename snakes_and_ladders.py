from os import system
import random

#these are the initiators for positions of mini pythons
a,b,c,d = 0,0,0,0

#these are the initiators for positions of large pythons
A,B,C,D,E,F = 0,0,0,0,0,0

#these are the initiators for random block subtractors if the player step on a large python
AA,BB,CC,DD,EE,FF = 0,0,0,0,0,0

#these are the initiators for positions of ladders
L1,L2,L3,L4,L5,L6 = 0,0,0,0,0,0

#these are the initiators for random block adders if the player step on a large python
LL1,LL2,LL3,LL4,LL5,LL6 = 0,0,0,0,0,0

#these are the positions corresponds when the player lands on the large snake
_A,_B,_C,_D,_E,_F = 0,0,0,0,0,0

#this are the positions corresponds when the player lands on the ladders
_L1,_L2,_L3,_L4,_L5,_L6 = 0,0,0,0,0,0


"""
this function provides the random numbers for each mini python, large python and subtractors, ladders and adders, as the criteria said
in the first run, pythons and ladders should be at random positions.
"""

def opening_randoms():
    global a,b,c,d 
    global A,B,C,D,E,F
    global AA,BB,CC,DD,EE,FF
    global L1,L2,L3,L4,L5,L6 
    global LL1,LL2,LL3,LL4,LL5,LL6

    #these are the positions of mini pythons
    
    a = random.randrange(3,100)
    b = random.randrange(3,100)
    c = random.randrange(3,100)
    d = random.randrange(3,100)

    #these are the positions of large snakes
    A = random.randrange(5,100)
    B = random.randrange(5,100)
    C = random.randrange(5,100)
    D = random.randrange(5,100)
    E = random.randrange(5,100)
    F = random.randrange(5,100)
    
    
    #these are the random numbers of blocks which will be subtracted from player landing on a large snake
    AA = random.randrange(3,51)
    BB = random.randrange(3,51)
    CC = random.randrange(3,51)
    DD = random.randrange(3,51)
    EE = random.randrange(3,51)
    FF = random.randrange(3,51)

    #these are the positions of ladders
    L1 = random.randrange(1,97)
    L2 = random.randrange(1,97)
    L3 = random.randrange(1,97)
    L4 = random.randrange(1,97)
    L5 = random.randrange(1,97)
    L6 = random.randrange(1,97)

    #these are the random numbers of blocks which will be subtracted from player landing on a ladders
    LL1 = random.randrange(1,31)
    LL2 = random.randrange(1,31)
    LL3 = random.randrange(1,31)
    LL4 = random.randrange(1,31)
    LL5 = random.randrange(1,31)
    LL6 = random.randrange(1,31)
    
    


def board():
    global c_tile
    board = [
        [100,99,98,97,96,95,94,93,92,91],
        [81,82,83,84,85,86,87,88,89,90],
        [80,79,78,77,76,75,74,73,72,71],
        [61,62,63,64,65,66,67,68,69,70],
        [60,59,58,57,56,55,54,53,52,51],
        [41,42,43,44,45,46,47,48,49,50],
        [40,39,38,37,36,35,34,33,32,31],
        [21,22,23,24,25,26,27,28,29,30],
        [20,19,18,17,16,15,14,13,12,11],
        [1,2,3,4,5,6,7,8,9,10]
       
            ]
    
    
    length_y = len(board)
    
    for i in range(0,length_y):    
        for j in board[i]:
            
            if c_tile == j:
                j = '0'
            else:
                j = '*'
            print(j,end = '  ')
        print("\n")
    
        


def randoms():
    
    global a,b,c,d
    global A,B,C,D,E,F
    global AA,BB,CC,DD,EE,FF
    global _A,_B,_C,_D,_E,_F
    global L1,L2,L3,L4,L5,L6
    global LL1, LL2,LL3,LL4,LL5,LL6
    global _L1,_L2,_L3,_L4,_L5,_L6
    global small_pythons
    global large_pythons
    global ladders
    global final_pos_large_pythons
    global final_pos_ladders

    
    
    first = {a,b,c,A,B,C,D,E,F,L1,L2,L3,L4,L5,L6}
    second = {b,c,d,A,B,C,D,E,F,L1,L2,L3,L4,L5,L6}
    third = {c,d,a,A,B,C,D,E,F,L1,L2,L3,L4,L5,L6}
    fourth = {d,a,b,A,B,C,D,E,F,L1,L2,L3,L4,L5,L6}
    
    FIRST = {A,B,C,D,E,a,b,c,d,L1,L2,L3,L4,L5,L6}
    SECOND = {B,C,D,E,F,a,b,c,d,L1,L2,L3,L4,L5,L6}
    THIRD = {C,D,E,F,A,a,b,c,d,L1,L2,L3,L4,L5,L6}
    FOURTH = {D,E,F,A,B,a,b,c,d,L1,L2,L3,L4,L5,L6}
    FIFTH = {E,F,A,B,C,a,b,c,d,L1,L2,L3,L4,L5,L6}
    SIXTH = {F,A,B,C,D,a,b,c,d,L1,L2,L3,L4,L5,L6}
    
    First = {L1,L2,L3,L4,L5,a,b,c,d,A,B,C,D,E,F}
    Second = {L2,L3,L4,L5,L6,a,b,c,d,A,B,C,D,E,F}
    Third = {L3,L4,L5,L6,L1,a,b,c,d,A,B,C,D,E,F}
    Fourth = {L4,L5,L6,L1,L2,a,b,c,d,A,B,C,D,E,F}
    Fifth = {L5,L6,L1,L2,L3,a,b,c,d,A,B,C,D,E,F}
    Sixth = {L6,L1,L2,L3,L4,a,b,c,d,A,B,C,D,E,F}
    
    
 
    game1 = 1
    
    while game1 == 1:
        
        if a in second:
            a = random.randrange(3,100)
        elif b in third:
            b = random.randrange(3,100)
        elif c in fourth:
            c = random.randrange(3,100)
        elif d in first:
            d = random.randrange(3,100)
        elif A in SECOND:
            A = random.randrange(5,100)
        elif B in THIRD:
            B = random.randrange(5,100)
        elif C in FOURTH:
            C = random.randrange(5,100)
        elif D in FIFTH:
            D = random.randrange(5,100)
        elif E in SIXTH:
            E = random.randrange(5,100)
        elif F in FIRST:
            F = random.randrange(5,100)
        elif L1 in Second:
            L1 = random.randrange(1,97)
        elif L2 in Third:
            L2 = random.randrange(1,97)
        elif L3 in Fourth:
            L3 = random.randrange(1,97)
        elif L4 in Fifth:
            L4 = random.randrange(1,97)
        elif L5 in Sixth:
            L5 = random.randrange(1,97)
        elif L6 in First:
            L6 = random.randrange(1,97)
            
                  
        else:
            game1 = 0
            
    
    #For Large Pythons
    game2 = 1
    while game2 == 1:        
        if A < AA or B < BB or C < CC or D < DD or E < EE or F < FF  :
            AA = random.randrange(3,51)
            BB = random.randrange(3,51)
            CC = random.randrange(3,51)
            DD = random.randrange(3,51)
            EE = random.randrange(3,51)
            FF = random.randrange(3,51)
            
        else:
            game2 = 0
            
    _A = A- AA
    _B = B- BB
    _C = C- CC
    _D = D- DD
    _E = E- EE
    _F = F- FF
    
    final_pos_large_pythons = _A,_B,_C,_D,_E,_F
    
    
    small_pythons = a,b,c,d
    large_pythons = A,B,C,D,E,F
    ladders = L1,L2,L3,L4,L5,L6
    
    _L1 = L1+ LL1
    _L2 = L2+ LL2
    _L3 = L3+ LL3
    _L4 = L4+ LL4
    _L5 = L5+ LL5
    _L6 = L6+ LL6
    
    game3 = 1
    while game3==1:
        if _L1 in large_pythons or _L2 in large_pythons or _L3 in large_pythons or _L4 in large_pythons or _L5 in large_pythons or _L6 in large_pythons:
            LL1 = random.randrange(1,31)
            LL2 = random.randrange(1,31)
            LL3 = random.randrange(1,31)
            LL4 = random.randrange(1,31)
            LL5 = random.randrange(1,31)
            LL6 = random.randrange(1,31)
            
            _L1 = L1+ LL1
            _L2 = L2+ LL2
            _L3 = L3+ LL3
            _L4 = L4+ LL4
            _L5 = L5+ LL5
            _L6 = L6+ LL6
        else:
            game3 = 0
    
    final_pos_ladders = _L1, _L2, _L3, _L4, _L5, _L6
    

def opening():
    global choice 
    global run
    global go_on
    global name
    
    print("Welcome to Python and Ladders!\n")
    
    print("[1] New Game")
    print("[2] View High Scores")
    print("[3] Quit")   
    choice = int(input())
    
    if choice == 1:
        name = input("Enter Player's name: ")
        pass
    elif choice == 2:
        system('cls')
        file = open("HigH_scores.txt", 'r')
        lines = file.readlines()
        arr1,arr2,arr3 = [],[],{}
        
        for x in lines:
            fields = x.split(',')
            arr1.append(int(fields[0]))
            arr2.append(fields[1])
            
            name = fields[1].replace("\n","")
            arr3[int(fields[0])] = name
        arr1.sort(reverse = True)
        con = 0
        for x in arr1:
            
            values = arr3.get(x)
            if con<3:
         
                con+=1
                print("\n",x,"-",values)
           
                
        file.close()
            
        run = 0
    elif choice == 3:
        go_on = 0
        
    
        


def game():
    
    global score
    global a,b,c,d
    global A,B,C,D,E,F
    global AA,BB,CC,DD,EE,FF
    global _A,_B,_C,_D,_E,_F
    global L1,L2,L3,L4,L5,L6
    global LL1, LL2,LL3,LL4,LL5,LL6
    global _L1,_L2,_L3,_L4,_L5,_L6
    global dice, run
    global small_pythons
    global large_pythons
    global ladders
    global final_pos_large_pythons
    global final_pos_ladders
    global c_tile 
    global isWon
    
    length_large_pythons = len(large_pythons)
    length_small_pythons = len(small_pythons)
    length_ladders = len(ladders)
    
    
    
    print(f"Player score : {score}")
    print(f"Mini Python blocks: {a} {b} {c} {d}\n")
    print(f"Large Pythons:\n{A} - {_A}\n{B} - {_B}\n{C} - {_C}\n{D} - {_D}\n{E} - {_E}\n{F} - {_F}\n\n")
    print(f"Ladders:\n{L1} - {_L1}\n{L2} - {_L2}\n{L3} - {_L3}\n{L4} - {_L4}\n{L5} - {_L5}\n{L6} - {_L6}\n\n")
    print(f"Current tile = {c_tile}\n")
    choice = input("Roll the dice? (Y/y or Q/q): \n")
    print("---------------------------------------------------------------------\n")
    
    if choice == 'Y' or choice == 'y':
        dice = random.randrange(1,7)
        print(f"Dice rolled a {dice}!")
        score += 1
        c_tile+= dice
        
        while True:
            if c_tile in small_pythons or c_tile in large_pythons or c_tile in ladders:
                
                if c_tile in small_pythons:
                        c_tile -= 3
                        print(f"A mini python caused you to stumble 3 blocks back to block {c_tile}! ")
                        input()
                    
                elif c_tile in large_pythons:
                    for i in range(0, length_large_pythons):
                        if c_tile == large_pythons[i]:
                            c_tile = final_pos_large_pythons[i]
                            print(f"Oh no! A Large python dragged you back to tile {c_tile}! ")
                            input()
                elif c_tile in ladders:
                    
                    for i in range(0, length_ladders):
                        if c_tile == ladders[i]:
                            c_tile = final_pos_ladders[i]
                            print(f"You landed on a ladder! You are now at tile {c_tile}! ")
                            input()
                    
            else:
                break
            
        if not(c_tile in small_pythons and c_tile in ladders and c_tile in large_pythons):
            
            print(f"Nothing happened... You are now at tile {c_tile}")
            input()
        
    elif choice == 'Q' or choice == 'q':
        print("Quit the game!\n\nThank You for Playing!")
        run = 0
 
            
    a = random.randrange(3,100)
    b = random.randrange(3,100)
    c = random.randrange(3,100)
    d = random.randrange(3,100)
    
    if c_tile >= 100:
        print("Congratulations! You have won!\n\nThank You for Playing!")      
        input()
        run=0

    if choice == 'Q' or choice == 'q':
        
        input()
        system('cls')
    system('cls')
    
   
go_on = 1
while go_on == 1:
    system('cls')
    run = 1
    score = 0
    dice = 0
    choice = 0
    c_tile = 0
    opening_randoms()
    opening()
    
    if go_on == 0:
        break
    while run==1: 
        system('cls')
        randoms()
        board()
        game()
        

    file = open("HigH_scores.txt", 'a')
    file.write(str(score)+"," + name + "\n")
    file.close()
    
   
    print("[R]eturn to the main menu: ")
    again = input()
    if again == 'R' or again == 'r':
        go_on=1
    else:
        go_on = 0
    
#prelims_snakes_and_ladders.py
