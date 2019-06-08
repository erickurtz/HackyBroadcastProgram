import urllib.request
from bs4 import BeautifulSoup
import re
import tkinter as Tk
from chesscomscraper import PlayerTracker



class Game:
    def __init__(self, gameArray):
        self.white = gameArray[0]
        self.whiteRating = int(gameArray[1])
        self.black = gameArray[2]
        self.blackRating = int(gameArray[3])
        self.whiteScore = self.parseScoreFromString(gameArray[4])
        self.blackScore = self.parseScoreFromString(gameArray[5])
        self.timeControl = gameArray[6]
        self.numMoves = int(gameArray[7])
        self.date = gameArray[8]

    def __str__(self):
        result ="White: " + self.white + " Rated: " + str(self.whiteRating) + "\n" + "Black: "+ self.black + " Rated: " + str(self.blackRating) + "\nResult: " + str(self.whiteScore) + " " + str(self.blackScore) + "\nTC: "+ self.timeControl + "\nMoves: "+ str(self.numMoves) + "\nDate: " + self.date
        return result

    def __eq__(self, other):
        if other != None: 
            return self.__dict__ == other.__dict__
        else:
            return False
    def parseScoreFromString(self, aScore):
        if aScore == "½":
            return 0.5
        elif aScore == "1":
            return 1
        elif aScore == "0":
            return 0


    
class ChessComMatchTracker:
    def __init__(self, master):
        self.winsFile = "homeScore.txt"
        self.lossesFile = "awayScore.txt"
        self.streakFile = "streak.txt"
        self.master = master
        self.start = False
        self.master.minsize(width=500,height=500)
        self.tracker = PlayerTracker()
        self.trackedUrl = Tk.StringVar()
        self.trackedUrl.set("No url")
        self.status = Tk.StringVar()
        self.status.set("Not Tracking")
        self.latestGame = None   
        self.homeScore = Tk.DoubleVar()
        self.awayScore = Tk.DoubleVar()
        self.totalGames = Tk.IntVar()
        self.streak = Tk.IntVar()
        self.homeScore.set(0.0)
        self.awayScore.set(0.0)
        self.totalGames.set(0)
        self.trackedPlayer = Tk.StringVar()
        self.opponentPlayer = Tk.StringVar()
        self.enterPlayer = Tk.Entry(self.master)
        self.trackedPlayer.set("Player 1")
        self.opponentPlayer.set("Player 2")
        self.startButton = Tk.Button(self.master, text = "Start", command = self.pressStart)
        self.inputName = Tk.Button(self.master, text = "Enter", command = self.setTrackerPlayer)
        
        self.resetMatch = Tk.Button(self.master, text = "Reset Match", command = self.resetScores)
        self.winLabel = Tk.Label(self.master, textvariable = self.homeScore)
        self.loseLabel = Tk.Label(self.master, textvariable = self.awayScore)
        self.streakLabel = Tk.Label(self.master, textvariable = self.streak)
        self.totalLabel = Tk.Label(self.master, textvariable = self.totalGames)


        self.winLabelText = Tk.Label(self.master, text = "Wins")
        self.lossLabelText = Tk.Label(self.master, text = "Losses")
        self.totalGamesLabel = Tk.Label(self.master, text = "Total")

        self.playerOneLabel = Tk.Label(self.master, textvariable = self.trackedPlayer)
        self.playerTwoLabel = Tk.Label(self.master, textvariable = self.opponentPlayer)

        self.urlLabel = Tk.Text(self.master, height=4, width=30, wrap="char")
    

        self.trackingLabel = Tk.Label(self.master, textvariable = self.status)
        
        
        self.playerOneLabel.grid(row=0, column =1)
        self.playerTwoLabel.grid(row=0, column =3)
        self.totalGamesLabel.grid(row=0,column=2)
        self.winLabel.grid(row=1, column =1)
        self.totalLabel.grid(row=1, column=2)
        self.loseLabel.grid(row=1, column=3)

        self.urlLabel.grid(row=2,columnspan=3)
        self.enterPlayer.grid(row=3, columnspan=2)
        self.inputName.grid(row=3, column=3)

        self.trackingLabel.grid(row=4, columnspan =2)
        self.startButton.grid(row=4, column=3)
        
    def getLatestGame(self):
        game1 = Game(self.tracker.getLatestGameFromURL(self.trackedUrl.get()))
        print (str(game1))
        print ("\n")
        return game1
        
    def updateFromGame(self, game):
        
        if self.latestGame == None:
            if self.trackedPlayer.get() != game.white:
                self.opponentPlayer.set(game.white)
            else:
                self.opponentPlayer.set(game.black)
            self.updateScores(game)
        elif self.latestGame == game:
            print ("do nothing")
        elif self.opponentPlayer.get() != game.white and self.opponentPlayer.get() != game.black:
            self.resetScores()
            if self.trackedPlayer.get() != game.white:
                self.opponentPlayer.set(game.white)
            else:
                self.opponentPlayer.set(game.black)
            self.updateScores(game)
        else:
            self.updateScores(game)
        self.latestGame = game

    def updateScores(self, game):
        if self.trackedPlayer.get() == game.white:
            self.homeScore.set(self.homeScore.get() + game.whiteScore)
            self.awayScore.set(self.awayScore.get() + game.blackScore)
            self.totalGames.set(self.totalGames.get() + 1)
            if game.whiteScore != 1:
                self.streak.set(0)
            else:
                self.streak.set(self.streak.get() + 1)
        else:
            self.homeScore.set(self.homeScore.get() + game.blackScore)
            self.awayScore.set(self.awayScore.get() + game.whiteScore)
            self.totalGames.set(self.totalGames.get() + 1)
            if game.blackScore != 1:
                self.streak.set(0)
            else:
                self.streak.set(self.streak.get() + 1)

        
    def resetScores(self):
        self.homeScore.set(0.0)
        self.awayScore.set(0.0)
        self.totalGames.set(0)
        self.streak.set(0)

        
    def track(self):
        self.master.after(20000, self.track)
        if self.start:
            self.updateFromGame(self.getLatestGame())
        
        
                       
    def pressStart(self):
        if(self.trackedPlayer.get() == ""):
            print("please enter a player") ##don't actually print anything
        else:
            self.start = not(self.start)
            if self.start:
                self.startButton["text"] = "Stop" 
                self.status.set("Tracking....")
                self.latestGame = self.getLatestGame()
            else:
                self.startButton["text"]="Start"
                self.status.set("Not Tracking")
                self.latestGame = None
            
    def setTrackerPlayer(self):
        self.trackedPlayer.set(self.enterPlayer.get())
        self.trackedUrl.set("https://www.chess.com/games/archive?username="+self.trackedPlayer.get())
        self.game = None
        self.urlLabel.delete('1.0', Tk.END)
        self.urlLabel.insert(Tk.END, self.trackedUrl.get())
            
            
def main():
    url = "https://www.chess.com/games/archive/hikaru"
    parser = PlayerTracker()
    game1 = Game (parser.getLatestGameFromURL(url))
    print (str(game1))

    
    root = Tk.Tk()
    gui= ChessComMatchTracker(root)
    root.after(20000, gui.track)
    root.mainloop()

main()
    
    
