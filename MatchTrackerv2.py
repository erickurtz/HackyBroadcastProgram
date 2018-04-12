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
            self.homeScore.set(this.homeScore.get() + 1)
            self.streak.set(this.streak.get() + 1)
            self.totalGames.set(this.totalGames.get() +1)
            writeToFile(winFile, str(homeScore.get()))
            writeToFile(streakFile, str(streak.get()))
            self.streakCheck()

        def loseAction():
            self.awayScore
            self.totalGames+=1
            self.streak = 0
            writeToFile(loseFile, str(awayScore))
            writeToFile(streakFile, str(streak))

        def drawAction():
            self.awayScore +=0.5
            self.homeScore +=0.5
            self.totalGames +=1
            self.streak = 0

            writeToFile(streakFile, str(streak))
            writeToFile(loseFile, str(awayScore))
            writeToFile(winFile, str(homeScore))

        
        def resetScores():
            self.awayScore = 0
            self.homeScore = 0
            self.streak = 0
            self.totalGames = 0
            writeToFile(loseFile, str(awayScore))
            writeToFile(winFile, str(homeScore))
            writeToFile(streakFile, str(streak))
            

        def newMatch():
            resetScores()
            self.nameOne = ""
            self.nameTwo = ""
            writeToFile(nameOneFile, nameOne)
            writeToFile(nameTwoFile, nameTwo)

        def hideFile(fileName):
            writeToFile(fileName, "")

        def updateNameOne(newName):
            self.nameOne = newName
            writeToFile(nameOneFile, nameOne)

        def updateNameTwo(newName):
            self.nameTwo = newName
            writeToFile(nameTwoFile, nameTwo)
        
        def streakCheck():
            if streak >= 10:
                writeToFile(adoptionFile, "Adoption.")
            
        
        

                        
            
