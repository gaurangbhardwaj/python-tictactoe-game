import os
import time
import sys

spacematrix=[[0,0,0],[0,0,0],[0,0,0]]
player=1

player1score=0
player2score=0

def GameOver(player):
    global spacematrix
    global player1score
    global player2score

    print("###################### Game Over #########################\n")
    print("\nplayer %d wins!!\n\n" % player)
    if(player==1):
        player1score=player1score+1
    elif(player==2):
        player2score=player2score+1

    spacematrix=[[0,0,0],[0,0,0],[0,0,0]]

    opt=str(input("Want another game? : y/n"))

    if(opt=='y' or opt=='Y'):
        for i in range(10,0,-1):
            os.system('cls')
            print("\n\nNew game will begin in ...%d" % i)
            time.sleep(0.5)
        StartGame()
    else:
        os.system('cls')
        print("\n\n---------------Final Scores--------------------\n\n")
        print("\nPlayer 1 Wins = %d\n\n" % player1score)
        print("\nPlayer 2 Wins = %d\n\n" % player2score)
        if(input("\n\nPress any key to exit game: ")):
            for i in range(10,0,-1):
                os.system('cls')
                print("\n\nGame closing...%d" % i)
                time.sleep(0.5)
            sys.exit(0)


def StartGame():
    global player
    player=1
    os.system('cls')
    if(input("Enter any key to start the game :: ")):
            GameBegin()

def ScoreCard():
    global spacematrix
    
    #for horizontal line matching
    if(not(spacematrix[0][0]==0)):
        if((spacematrix[0][0]==spacematrix[0][1])and(spacematrix[0][1]==spacematrix[0][2])):
             GameOver(spacematrix[0][0])
   
    if(not(spacematrix[1][0]==0)):
        if((spacematrix[1][0]==spacematrix[1][1])and(spacematrix[1][1]==spacematrix[1][2])):
             GameOver(spacematrix[1][0])
   
    if(not(spacematrix[2][0]==0)):
        if((spacematrix[2][0]==spacematrix[2][1])and(spacematrix[2][1]==spacematrix[2][2])):
             GameOver(spacematrix[2][0])

     #for vertical line matching
    if(not(spacematrix[0][0]==0)):
        if((spacematrix[0][0]==spacematrix[1][0])and(spacematrix[1][0]==spacematrix[2][0])):
             GameOver(spacematrix[0][0])
   
    if(not(spacematrix[0][1]==0)):
        if((spacematrix[0][1]==spacematrix[1][1])and(spacematrix[1][1]==spacematrix[2][1])):
             GameOver(spacematrix[0][1])
   
    if(not(spacematrix[0][2]==0)):
        if((spacematrix[0][2]==spacematrix[1][2])and(spacematrix[1][2]==spacematrix[2][2])):
             GameOver(spacematrix[0][2])   

    
    #for cross matching
    if(not(spacematrix[0][0]==0)):
        if((spacematrix[0][0]==spacematrix[1][1])and(spacematrix[1][1]==spacematrix[2][2])):
            GameOver(spacematrix[0][0])
    
    if(not(spacematrix[0][2]==0)):
        if((spacematrix[0][2]==spacematrix[1][1])and(spacematrix[1][1]==spacematrix[2][0])):
            GameOver(spacematrix[0][2])

    
def GameBegin():
    global spacematrix
    global player1score
    global player2score

    for i in range(0,9):
        os.system('cls')
        print("\nPlayer 1 Wins = %d\n\n" % player1score)
        print("\nPlayer 2 Wins = %d\n\n" % player2score)
        for i in range(0,3):
            for j in range(0,3):
                if(spacematrix[i][j]==1):
                    print('O',end=" ")
                elif(spacematrix[i][j]==2):
                    print('X',end=" ")
                else:
                    print('-',end=" ")
            print("")
        ScoreCard()
        if(player==1):
            PlayerOne()
        else:
            PlayerSecond()



def BlockCheckerMarker(block, player):
    global spacematrix
    if(block==1):
        if(not (spacematrix[0][0]==0)):
            return 0
        else:
            spacematrix[0][0]=player
            return 1
    
    elif(block==2):
        if(not (spacematrix[0][1]==0)):
            return 0
        else:
            spacematrix[0][1]=player
            return 1
    
    elif(block==3):
        if(not(spacematrix[0][2]==0)):
            return 0
        else:
            spacematrix[0][2]=player
            return 1
    
    elif(block==4):
        if(not(spacematrix[1][0]==0)):
            return 0
        else:
            spacematrix[1][0]=player
            return 1
    
    elif(block==5):
        if(not(spacematrix[1][1]==0)):
            return 0
        else:
            spacematrix[1][1]=player
            return 1
    
    elif(block==6):
        if(not(spacematrix[1][2]==0)):
            return 0
        else:
            spacematrix[1][2]=player
            return 1

    elif(block==7):
        if(not(spacematrix[2][0]==0)):
            return 0
        else:
            spacematrix[2][0]=player
            return 1

    elif(block==8):
        if(not(spacematrix[2][1]==0)):
            return 0
        else:
            spacematrix[2][1]=player
            return 1

    elif(block==9):
        if(not(spacematrix[2][2]==0)):
            return 0
        else:
            spacematrix[2][2]=player
            return 1
    else:
        print("\n\nInvalid block")
        return 0
    
        

    
def PlayerOne():
    global player
    player=1
    print("Player 1 turn : ")
    userInput=int(input("Enter the desired Block number : "))
    if(BlockCheckerMarker(userInput,1)):
        player=2

    else:
        print("\n\nBlock already used!!")
        PlayerOne()

def PlayerSecond():
    global player
    player=2
    print("Player 2 turn : ")
    userInput=int(input("Enter the desired Block number : "))
    if(BlockCheckerMarker(userInput,2)):
        player=1
    else:
        print("\n\nBlock already used!!")
        PlayerSecond()
               
StartGame()