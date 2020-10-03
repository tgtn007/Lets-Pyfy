import pyttsx3
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

rate=engine.getProperty("rate")
engine.setProperty("rate",125)

def spk(ad) :
    engine.say(ad)
    engine.runAndWait()
    

count=0
board=[['   ','|','   ','|','   '],['---','|','---','|','---'],['   ','|','   ','|','   '],['---','|','---','|','---'],['   ','|','   ','|','   ']]
win_combo=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
sign=['X','O']
position=[[' '],[0,0],[0,2],[0,4],[2,0],[2,2],[2,4],[4,0],[4,2],[4,4]]
rel_pos=[1,2,3,4,5,6,7,8,9]
corn=[1,3,7,9]
edge=[2,4,6,8]


def print_board(board) :
    for i in board :
        for j in i :
            print(j,end=' ')
        print('\n')


def move(s,i,j) :
    board[i][j]=s


def win_chk(player_sign,AI_sign) :
    for i in win_combo :
        a,b,c=i
        x1,y1=position[a]
        x2,y2=position[b]
        x3,y3=position[c]
        if board[x1][y1]==board[x2][y2]==board[x3][y3]==player_sign :
            return 1
            break
        elif board[x1][y1]==board[x2][y2]==board[x3][y3]==AI_sign :
            return -1
            break

def chk_opp(AI_sign,player_sign) :
    ss=AI_sign
    e=0
    for j in range(2) :
        for i in win_combo :
            a,b,c=i
            x1,y1=position[a]
            x2,y2=position[b]
            x3,y3=position[c]   
            if board[x1][y1]==board[x2][y2]==ss and board[x3][y3]=='   ' :
                return c 
                e=1
                break 
            elif board[x1][y1]==board[x3][y3] ==ss and board[x2][y2]=='   ' :
                return b
                e=1
                break
            elif board[x2][y2]==board[x3][y3] ==ss and board[x1][y1]=='   ' :
                return a
                e=1
                break
            else :
                continue
        if e==1 :
            break
        ss=player_sign
    return 0
        


def play(count) :
    print("\n\n\n")
    print_board(board)
    print("\n\n\n")
    while True :
        spk("Please choose your sign between 'X' and 'O' ")
        player_sign=input("Please choose your sign ('X' or 'O') : ")
        if player_sign == 'X' or 'x' :
            player_sign = ' X '
            AI_sign=' O '
            break
        elif player_sign == 'O' or 'o' :
            player_sign = ' O '
            AI_sign=' X ' 
            break
        else :
            spk("Invalid Sign ! Please choose either 'X' or 'O'......")
            print("Invalid Sign ! Please choose either 'X' or 'O'......")
    print("\n\t\t\t 0  :  Easy \n\n\t\t\t 1  :  Medium\n\n\n")
    spk("Please choose a difficulty Level Enter 0 for Easy or Enter 1 for Medium Difficulty Level.")
    lvl=int(input("Please choose a difficulty Level : "))
    while True :
        if count%2==0 :
            spk("Your Turn.")
            print("\n\n\t\t\t_____________Player's  Turn____________\t\t\t\n\n")
            print("\n")
            print_board(board)
            print("\n\n\n")            
            while True :
                spk("Please Enter a position between 1-9 that is empty. ")
                c=int(input("Please Enter a position between 1-9 that is empty : "))
                i,j=position[c]
                if board[i][j]=='   ' :
                    move(player_sign,i,j)
                    count=count+1
                    print("\n\n\n")
                    print_board(board)
                    print("\n\n\n")
                    break
                else :
                    spk("Sorry this position is already occupied ....please choose a different position.")
                    print("\nSorry this position is already occupied ....please choose a different position.\n\n")
        else :
            spk("Computer's Turn.")
            print("\n\n\t\t\t_____________Computer's  Turn____________\t\t\t\n\n")
            while True :
                if lvl==0 :
                    i=random.randrange(0,5,2)
                    j=random.randrange(0,5,2)
                    if board[i][j]=='   ' :
                        move(AI_sign,i,j)
                        count=count+1
                        print("\n\n\n")
                        print_board(board)
                        print("\n\n\n")
                        break
                elif lvl==1 :
                    if count>2 :
                        d=chk_opp(AI_sign,player_sign)
                        if d==0 :
                           d=random.choice(edge)

                    else :
                        if c==5 :
                            d=random.choice(corn)
                        else :
                            d=5
                    i,j=position[d]
                    if board[i][j]=='   ' :
                        move(AI_sign,i,j)
                        count=count+1
                        print("\n\n\n")
                        print_board(board)
                        print("\n\n\n")
                        break                    
        w=win_chk(player_sign,AI_sign)
        if w==1 :
            spk("Player Wins.....Computer Loses.")
            print("Player Wins.....")
            break
        elif w==-1 :
            spk("Computer Wins......Player Loses.")
            print("Player Loses......")
            break
        if count==9 :
            spk("It is Draw.")
            print(".....Draw....")
            break

play(count)
