import Tkinter as tk

class matchTracker:
    def __init__(self, master):
        self.winFile = "wins.txt"
        self.loseFile = "losses.txt"
        self.streakFile = "streak.txt"
        self.nameOneFile = "name1.txt"
        self.nameTwoFile = "name2.txt"
        self.adoptionFile = "adoption.txt"
        self.master = master
        master.title = "MatchTracker v2.0"


        self.homeScore = DoubleVar()
        self.awayScore = DoubleVar()
        self.totalGames = IntVar()
        self.streak = IntVar()

        
        self.homeScore.set(0.0)
        self.awayScore.set(0.0)
        self.totalGames.set(0)
        self.streak.set(0)
        self.nameOne =stringVar()
        self.nameTwo =stringVar()

        self.nameOne.set("")
        self.nameTwo.set("")

        winLable = Lable(parent, self

        def writeToFile(fileName, toWrite):
            file = open(fileName, "w+")
            file.write(toWrite)
            file.close()

        def winAction():
            ##update display ?
            self.homeScore.set(self.homeScore.get() + 1)
            self.streak.set(self.streak.get() + 1)
            self.totalGames.set(self.totalGames.get() +1)
            writeToFile(winFile, str(self.homeScore.get()))
            writeToFile(streakFile, str(self.streak.get()))
            self.streakCheck()

        def loseAction():
            self.awayScore.set(self.awayScore.get() + 1))
            self.totalGames.set(self.totalGames.get() + 1)
            self.streak.set(0)
            writeToFile(loseFile, str(self.awayScore.get()))
            writeToFile(streakFile, str(self.streak.get()))

        def drawAction():
            self.awayScore.set(self.awayScore.get() + 0.5)
            self.homeScore.set(self.homeScore.get()  + 0.5)
            self.totalGames.set(self.homeScore.get() + 0.5)
            self.streak.set(0). 

            writeToFile(streakFile, str(self.streak.get()))
            writeToFile(loseFile, str(self.awayScore.get()))
            writeToFile(winFile, str(self.homeScore.get()))

        
        def resetScores():
            self.awayScore.set(0)
            self.homeScore.set(0)
            self.streak.set(0)
            self.totalGames.set(0)
            writeToFile(loseFile, str(self.awayScore.get()))
            writeToFile(winFile, str(self.homeScore.get()))
            writeToFile(streakFile, str(self.streak.get()))
            

        def newMatch():
            resetScores()
            self.nameOne.set("")
            self.nameTwo.set("")
            writeToFile(nameOneFile, nameOne.get())
            writeToFile(nameTwoFile, nameTwo.get())

        def hideFile(fileName):
            writeToFile(fileName, "")

        def updateNameOne(newName):
            self.nameOne.set(newName)
            writeToFile(nameOneFile, nameOne.get())

        def updateNameTwo(newName):
            self.nameTwo.set(newName)
            writeToFile(nameTwoFile, nameTwo.get())
        
        def streakCheck():
            if streak.get() >= 10:
                writeToFile(adoptionFile, "Adoption.")
            
        
        

                        
            
