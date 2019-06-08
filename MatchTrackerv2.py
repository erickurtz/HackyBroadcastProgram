import tkinter as Tk

class MatchTracker:
    def __init__(self, master):
        self.winFile = "wins.txt"
        self.loseFile = "losses.txt"
        self.drawFile = "draws.txt" 
        self.streakFile = "streak.txt"
        self.nameOneFile = "name1.txt"
        self.nameTwoFile = "name2.txt"
        self.adoptionFile = "adoption.txt"
        self.master = master
        master.title = "MatchTracker v2.0"


        self.homeScore = Tk.DoubleVar()
        self.awayScore = Tk.DoubleVar()
        self.numDraws = Tk.IntVar()
        self.totalGames = Tk.IntVar()
        self.streak = Tk.IntVar()

        
        self.homeScore.set(0.0)
        self.awayScore.set(0.0)
        self.totalGames.set(0)
        self.numDraws.set(0)
        self.streak.set(0)
        self.nameOne = Tk.StringVar()
        self.nameTwo = Tk.StringVar()
        self.nameOne.set("Player 1")
        self.nameTwo.set("Player 2")

        self.nameOneEntry = Tk.StringVar()
        self.nameTwoEntry = Tk.StringVar()
        
        self.winButton = Tk.Button(self.master, text = "Win", command = self.winAction)
        self.loseButton = Tk.Button(self.master, text = "Loss", command = self.loseAction)
        self.drawButton = Tk.Button(self.master, text = "Draw", command = self.drawAction)
        self.resetScoresButton = Tk.Button(self.master, text = "Reset Score", command = self.resetScores)
        self.resetMatch = Tk.Button(self.master, text = "Reset Match", command = self.resetMatch)
        self.winLabel = Tk.Label(self.master, textvariable = self.homeScore)
        self.loseLabel = Tk.Label(self.master, textvariable = self.awayScore)
        self.streakLabel = Tk.Label(self.master, textvariable = self.streak)
        self.totalLabel = Tk.Label(self.master, textvariable = self.totalGames)

        self.winLabelText = Tk.Label(self.master, text = "Wins")
        self.lossLabelText = Tk.Label(self.master, text = "Losses")
        self.totalGamesLabel = Tk.Label(self.master, text = "Total")

        self.enterPlayerOne = Tk.Entry(self.master, textvariable = self.nameOneEntry)
        self.enterPlayerTwo = Tk.Entry(self.master, textvariable = self.nameTwoEntry)

        self.changePlayerOne = Tk.Button(self.master, text = "Set", command = self.updateNameOne )
        self.changePlayerTwo = Tk.Button(self.master, text = "Set", command = self.updateNameTwo )
        self.playerOneLabel = Tk.Label(self.master, textvariable = self.nameOne)
        self.playerTwoLabel = Tk.Label(self.master, textvariable = self.nameTwo)


        self.playerOneLabel.grid(row=0, column =1)
        self.playerTwoLabel.grid(row=0, column =3)
        self.totalGamesLabel.grid(row=0,column=2)
        self.winLabel.grid(row=1, column =1)
        self.totalLabel.grid(row=1, column=2)
        self.loseLabel.grid(row=1, column=3)
        self.winButton.grid(row=2, column=1)
        self.drawButton.grid(row=2, column=2)
        self.loseButton.grid(row=2,column=3)
        self.resetScoresButton.grid(row=3,column=1)
        self.resetMatch.grid(row=3,column=3)
        self.changePlayerOne.grid(row=4, column =1)
        self.changePlayerTwo.grid(row=4, column=3)
        self.enterPlayerOne.grid(row=5,column=1)
        self.enterPlayerTwo.grid(row=5,column=3)


    def writeToFile(self,fileName, toWrite):
        file = open(fileName, "w+")
        file.write(toWrite)
        file.close()
                        

    def winAction(self):
        ##update display ?
        self.homeScore.set(self.homeScore.get() + 1)
        self.streak.set(self.streak.get() + 1)
        self.totalGames.set(self.totalGames.get() +1)
        self.writeToFile(self.winFile, str(self.homeScore.get()))
        self.writeToFile(self.streakFile, str(self.streak.get()))
        self.streakCheck()

    def loseAction(self):
        self.awayScore.set(self.awayScore.get() + 1)
        self.totalGames.set(self.totalGames.get() + 1)
        self.streak.set(0)
        self.writeToFile(self.loseFile, str(self.awayScore.get()))
        self.writeToFile(self.streakFile, str(self.streak.get()))

    def drawAction(self):
        self.awayScore.set(self.awayScore.get() + 0.5)
        self.homeScore.set(self.homeScore.get()  + 0.5)
        self.totalGames.set(self.homeScore.get() + 0.5)
        self.numDraws.set(self.numDraws.get() + 1)
        self.streak.set(0)

        self.writeToFile(self.streakFile, str(self.streak.get()))
        self.writeToFile(self.loseFile, str(self.awayScore.get()))
        self.writeToFile(self.winFile, str(self.homeScore.get()))
        self.writeToFile(self.drawFile, str(self.numDraws.get()))
        
        
    def resetScores(self):
        self.awayScore.set(0)
        self.homeScore.set(0)
        self.streak.set(0)
        self.totalGames.set(0)
        self.writeToFile(self.loseFile, str(self.awayScore.get()))
        self.writeToFile(self.winFile, str(self.homeScore.get()))
        self.writeToFile(self.streakFile, str(self.streak.get()))
            

    def resetMatch(self):
        self.resetScores()
        self.nameOne.set("")
        self.nameTwo.set("")
        self.writeToFile(self.nameOneFile, self.nameOne.get())
        self.writeToFile(self.nameTwoFile, self.nameTwo.get())

    def hideFile(self,fileName):
        self.writeToFile(fileName, "")

    def updateNameOne(self):
        self.nameOne.set(self.nameOneEntry.get())
        self.writeToFile(self.nameOneFile, self.nameOne.get())

    def updateNameTwo(self):
        self.nameTwo.set(self.nameTwoEntry.get())
        self.writeToFile(self.nameTwoFile, self.nameTwo.get())
        
    def streakCheck(self):
        if self.streak.get() >= 10:
                self.writeToFile(self.adoptionFile, "Adoption.")

        

def main():
    root = Tk.Tk()
    gui=MatchTracker(root)
    root.mainloop()

main()
    

                        
            
