import string
import random
from random import randrange
import numpy as np

class Bot:

    predictionlist = np.array([1.0/3.0,1.0/3.0,1.0/3.0])
    transitionmatrix = np.array([[1.0/3.0,1.0/3.0,1.0/3.0],
                            [1.0/3.0,1.0/3.0,1.0/3.0],
                            [1.0/3.0,1.0/3.0,1.0/3.0]])
    lastMove = ""
    currentMove = ""
    totalMovesAfterR = 0
    totalMovesAfterP = 0
    totalMovesAfterS = 0
    RRCounter = 0
    RPCounter = 0
    RSCounter = 0
    PRCounter = 0
    PPCounter = 0
    PSCounter = 0
    SRCounter = 0
    SPCounter = 0
    SSCounter = 0
    

    def __init__(self):
        lastMove = ""
        currentMove = ""
        totalMovesAfterR = 0
        totalMovesAfterP = 0
        totalMovesAfterS = 0
        RRCounter = 0
        RPCounter = 0
        RSCounter = 0
        PRCounter = 0
        PPCounter = 0
        PSCounter = 0
        SRCounter = 0
        SPCounter = 0
        SSCounter = 0
        predictionlist = [1.0/3.0,1.0/3.0,1.0/3.0]
        transitionmatrix = [[1.0/3.0,1.0/3.0,1.0/3.0],
                            [1.0/3.0,1.0/3.0,1.0/3.0],
                            [1.0/3.0,1.0/3.0,1.0/3.0]]

        #print(predictionlist)


    def getpredictionlist(self):
        return self.predictionlist

    def setLastMove(self,l):
        self.lastMove = l
    def setCurrentMove(self,c):
        self.currentMove = c

    def predictOpponentsMove(self):
        if (self.getpredictionlist()[0]==self.getpredictionlist()[1]) & (self.getpredictionlist()[1]==self.getpredictionlist()[2]):
            num = randrange(3)
            #print(num)
            if num==0:
                return "R"
            elif num==1:
                return "P"
            elif num==2:
                return "S"
            else:
                return "Error"
            
        else:
            if (self.getpredictionlist()[1]>self.getpredictionlist()[0]) & (self.getpredictionlist()[1]>self.getpredictionlist()[2]):
                return "P"
            elif (self.getpredictionlist()[2]>self.getpredictionlist()[0]) & (self.getpredictionlist()[2]>self.getpredictionlist()[1]):
                return "S"
            else:
                return "R"

    def updateMatrix(self):
        if self.lastMove == "R":
            self.totalMovesAfterR+=1
            if self.currentMove == "R":
                self.RRCounter+=1
            elif self.currentMove == "P":
                self.RPCounter+=1
            elif self.currentMove == "S":
                self.RSCounter+=1
            self.transitionmatrix[0][0] = float(self.RRCounter)/float(self.totalMovesAfterR)
            self.transitionmatrix[0][1] = float(self.RPCounter)/float(self.totalMovesAfterR)
            self.transitionmatrix[0][2] = float(self.RSCounter)/float(self.totalMovesAfterR)
        elif self.lastMove == "P":
            self.totalMovesAfterP+=1
            if self.currentMove == "R":
                self.PRCounter+=1
            elif self.currentMove == "P":
                self.PPCounter+=1
            elif self.currentMove == "S":
                self.PSCounter+=1
            self.transitionmatrix[1][0] = float(self.PRCounter)/float(self.totalMovesAfterP)
            self.transitionmatrix[1][1] = float(self.PPCounter)/float(self.totalMovesAfterP)
            self.transitionmatrix[1][2] = float(self.PSCounter)/float(self.totalMovesAfterP)
        elif self.lastMove == "S":
            self.totalMovesAfterS+=1
            if self.currentMove == "R":
                self.SRCounter+=1
            elif self.currentMove == "P":
                self.SPCounter+=1
            elif self.currentMove == "S":
                self.SSCounter+=1
            self.transitionmatrix[2][0] = float(self.SRCounter)/float(self.totalMovesAfterS)
            self.transitionmatrix[2][1] = float(self.SPCounter)/float(self.totalMovesAfterS)
            self.transitionmatrix[2][2] = float(self.SSCounter)/float(self.totalMovesAfterS)
        #print(self.transitionmatrix)

    def updateList(self):
        self.predictionlist = np.dot(self.predictionlist,self.transitionmatrix)
        #print(self.predictionlist)

    def counterOpponentsMove(self):
        opponentsmove = self.predictOpponentsMove()
        if opponentsmove == "R":
            return "P"
        elif opponentsmove == "P":
            return "S"
        elif opponentsmove == "S":
            return "R"
        else:
            return "Error"



class RPS:
    playing = 1
    playcounter = 1
    yourLastMove = ""
    yourMove = ""
    bot = Bot()
    botWins = 0
    yourWins = 0
    ties = 0
    botWinPercentage = 0.0
    yourWinPercentage = 0.0
    tiePercentage = 0.0

    
        


    
    while(playing == 1):

        
        if playcounter > 1:
            yourLastMove = yourMove
            yourMove = ""

        


        
        print("Welcome to Rock Paper Scissors")
        yourMove = input("What is your move? (R(1), P(2), or S(3)): ")
        #hlist = ["R","P","S"]
        #yourMove = random.choice(hlist)
        if(yourMove == "1"):
            yourMove = "R"
        elif(yourMove == "2"):
            yourMove = "P"
        elif(yourMove == "3"):
            yourMove = "S"
            
        if(playcounter>1):
            bot.setLastMove(yourLastMove)
            bot.setCurrentMove(yourMove)
            bot.updateMatrix()
            bot.updateList()
        botMove = bot.counterOpponentsMove()
        #print(yourMove, botMove)
        if yourMove == "R":
            print("You chose Rock")
            if botMove == "R":
                print("Bot chose Rock")
                print("Tie")
                ties+=1
            elif botMove == "P":
                print("Bot chose Paper")
                print("Bot Wins")
                botWins+=1
                botWinPercentage = botWins/playcounter
                yourWinPercentage = yourWins/playcounter
                playcounter+=1
            elif botMove == "S":
                print("Bot chose Scissors")
                print("You Win")
                yourWins+=1
                botWinPercentage = botWins/playcounter
                yourWinPercentage = yourWins/playcounter
                playcounter+=1
            else:
                print("error, game stopped")
                playing = 0

        if yourMove == "P":
            print("You chose paper")
            if botMove == "R":
                print("Bot chose Rock")
                print("You win")
                yourWins +=1
                botWinPercentage = botWins/playcounter
                yourWinPercentage = yourWins/playcounter
                playcounter+=1
            elif botMove == "P":
                print("Bot chose Paper")
                print("Tie")
                ties+=1
            elif botMove == "S":
                print("Bot chose Scissors")
                print("Bot wins")
                botWins+=1
                botWinPercentage = botWins/playcounter
                yourWinPercentage = yourWins/playcounter
                playcounter+=1
                
            else:
                print("error")
                playing = 0

        if yourMove == "S":
            print("You chose scissors")
            if botMove == "R":
                print("Bot chose Rock")
                print("Bot wins")
                botWins+=1
                botWinPercentage = botWins/playcounter
                yourWinPercentage = yourWins/playcounter
                playcounter+=1
            elif botMove == "P":
                print("Bot chose Paper")
                print("You win")
                yourWins+=1
                botWinPercentage = botWins/playcounter
                yourWinPercentage = yourWins/playcounter
                playcounter+=1
            elif botMove == "S":
                print("Bot chose Scissors")
                print("Tie")
                ties+=1
            else:
                print("error")
                playing = 0

        

        print("Bot Win Percentage is", botWinPercentage)
        print("Human Win Percentage is", yourWinPercentage)
        print()
        print()

        

        #if(playcounter > 200):
            #playing = 0
        
       # cont = input("Do you want to continue?(Y or N): ")
       # if cont == "Y":
        #    print("Ok! Playing next game")
        #    playing = 1
       # elif cont == "N":
        #    print("Game has stopped")
        #    playing = 0
       # else:
         #   print("Error, Game Stopped")
          #  playing = 0

        
