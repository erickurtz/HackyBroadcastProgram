import tkinter as Tk

class MatchTracker:
    def __init__(self, master):
        self.winFile = "p1_tc1.txt"
        self.loseFile = "p2_tc1.txt"
        self.winFile2 = "p1_tc2.txt"
        self.loseFile2 = "p2_tc2.txt"
        self.winFile3 = "p1_tc3.txt"
        self.loseFile3 = "p2_tc3.txt"

        
        self.streakFile = "streak.txt"
        self.nameOneFile = "name1.txt"
        self.nameTwoFile = "name2.txt"
        self.adoptionFile = "adoption.txt"
        self.master = master
        master.title = "MatchTracker v2.0"

        self.homeScore = Tk.DoubleVar()
        self.awayScore = Tk.DoubleVar()

        self.home1 = Tk.DoubleVar()
        self.away1 = Tk.DoubleVar()

        
        self.home2 = Tk.DoubleVar()
        self.away2 = Tk.DoubleVar()

        self.home3 = Tk.DoubleVar()
        self.away3 = Tk.DoubleVar()



        
        self.totalGames = Tk.IntVar()
        self.streak = Tk.IntVar()

        
        self.homeScore.set(0.0)
        self.awayScore.set(0.0)

        
        self.home1.set(0.0)
        self.away1.set(0.0)
        self.home2.set(0.0)
        self.away2.set(0.0)
        self.home3.set(0.0)
        self.home3.set(0.0)



        
        self.totalGames.set(0)
        self.streak.set(0)
        self.nameOne = Tk.StringVar()
        self.nameTwo = Tk.StringVar()
        self.nameOne.set("Player 1")
        self.nameTwo.set("Player 2")

        self.nameOneEntry = Tk.StringVar()
        self.nameTwoEntry = Tk.StringVar()
        
        self.winButtonTc1 = Tk.Button(self.master, text = "Win 5", command = self.winAction)
        self.loseButtonTc1 = Tk.Button(self.master, text = "Win 5", command = self.loseAction)
        self.drawButtonTc1 = Tk.Button(self.master, text = "Draw 5", command = self.drawAction)  
        self.winButtonTc2 = Tk.Button(self.master, text = "Win 3", command = self.winAction_two)
        self.loseButtonTc2 = Tk.Button(self.master, text = "Win 3", command = self.loseAction_two)
        self.drawButtonTc2 = Tk.Button(self.master, text = "Draw 3", command = self.drawAction_two)
        self.winButtonTc3 = Tk.Button(self.master, text = "Win 1", command = self.winAction_three)
        self.loseButtonTc3 = Tk.Button(self.master, text = "Win 1", command = self.loseAction_three)
        self.drawButtonTc3 = Tk.Button(self.master, text = "Draw 1", command = self.drawAction_three)



        self.winLabel = Tk.Label(self.master, textvariable = self.homeScore)
        self.loseLabel = Tk.Label(self.master, textvariable = self.awayScore)
        self.streakLabel = Tk.Label(self.master, textvariable = self.streak)
        self.totalLabel = Tk.Label(self.master, textvariable = self.totalGames)

  

        self.winLabelOne = Tk.Label(self.master, textvariable = self.home1)
        self.loseLabelOne = Tk.Label(self.master, textvariable = self.away1)

        self.winLabelTwo = Tk.Label(self.master, textvariable = self.home2)
        self.loseLabelTwo = Tk.Label(self.master, textvariable = self.away2)

        self.winLabelThree = Tk.Label(self.master, textvariable = self.home3)
        self.loseLabelThree = Tk.Label(self.master, textvariable = self.away3)

        self.playerOneLabel = Tk.Label(self.master, textvariable = self.nameOne)
        self.playerTwoLabel = Tk.Label(self.master, textvariable = self.nameTwo)

        self.playerOneLabel.grid(row=0, column =0)
        self.playerTwoLabel.grid(row=0, column =4)
        
        self.winLabel.grid(row=1, column =0)
        self.totalLabel.grid(row=1, column=2)
        self.loseLabel.grid(row=1, column=4)

        
        self.winLabelOne.grid(row=2,column=0)
        self.winButtonTc1.grid(row=2, column=1)
        self.drawButtonTc1.grid(row=2, column=2)
        self.loseButtonTc1.grid(row=2,column=3)
        self.loseLabelTwo.grid(row=2,column=4)


        self.winLabelTwo.grid(row=3,column=0)
        self.winButtonTc2.grid(row=3, column=1)
        self.drawButtonTc2.grid(row=3, column=2)
        self.loseButtonTc2.grid(row=3,column=3)
        self.loseLabelTwo.grid(row=3,column=4)

        self.winLabelThree.grid(row=4,column=0)
        self.winButtonTc3.grid(row=4, column=1)
        self.drawButtonTc3.grid(row=4, column=2)
        self.loseButtonTc3.grid(row=4,column=3)
        self.loseLabelThree.grid(row=4,column=4)
        
    def writeToFile(self,fileName, toWrite):
        file = open(fileName, "w+")
        file.write(toWrite)
        file.close()
                        

    def winAction_two(self):
        ##update display ?
        self.homeScore.set(self.homeScore.get()+1)
        self.home2.set(self.home2.get() + 1)
        self.streak.set(self.streak.get() + 1)
        self.totalGames.set(self.totalGames.get() +1)
        self.writeToFile(self.winFile2, str(self.home2.get()))
        self.writeToFile(self.streakFile, str(self.streak.get()))
        self.streakCheck()

    def loseAction_two(self):
        self.away2.set(self.away2.get() + 1)
        self.awayScore.set(self.awayScore.get()+1)
        self.totalGames.set(self.totalGames.get() + 1)
        self.streak.set(0)
        self.writeToFile(self.loseFile2, str(self.away2.get()))
        self.writeToFile(self.streakFile, str(self.streak.get()))

    def drawAction_two(self):


        self.homeScore.set(self.homeScore.get() +0.5)
        self.awayScore.set(self.awayScore.get() + 0.5)
        
        self.away2.set(self.away2.get() + 0.5)
        self.home2.set(self.home2.get()  + 0.5)
        self.totalGames.set(self.totalGames.get() + 1)
        self.streak.set(0)

        self.writeToFile(self.streakFile, str(self.streak.get()))
        self.writeToFile(self.loseFile, str(self.away2.get()))
        self.writeToFile(self.winFile, str(self.home2.get()))
        


        
    def winAction_three(self):


        self.homeScore.set(self.homeScore.get()+1)
        ##update display ?
        self.home3.set(self.home3.get() + 1)
        self.streak.set(self.streak.get() + 1)
        self.totalGames.set(self.totalGames.get() +1)
        self.writeToFile(self.winFile3, str(self.home3.get()))
        self.writeToFile(self.streakFile, str(self.streak.get()))
        self.streakCheck()

    def loseAction_three(self):

        self.awayScore.set(self.awayScore.get() + 1)


        self.away3.set(self.away3.get() + 1)
        self.totalGames.set(self.totalGames.get() + 1)
        self.streak.set(0)
        self.writeToFile(self.loseFile3, str(self.away3.get()))
        self.writeToFile(self.streakFile, str(self.streak.get()))

    def drawAction_three(self):

        
        self.homeScore.set(self.homeScore.get() +0.5)
        self.awayScore.set(self.awayScore.get() + 0.5)


        
        self.away3.set(self.away3.get() + 0.5)
        self.home3.set(self.home3.get()  + 0.5)
        self.totalGames.set(self.totalGames.get() + 1)
        self.streak.set(0)

        self.writeToFile(self.streakFile, str(self.streak.get()))
        self.writeToFile(self.loseFile3, str(self.away3.get()))
        self.writeToFile(self.winFile3, str(self.home3.get()))
        


    def winAction(self):
        ##update display ?

        
        
        self.home1.set(self.home1.get() + 1)

        self.homeScore.set(self.homeScore.get()+1)

        self.streak.set(self.streak.get() + 1)
        self.totalGames.set(self.totalGames.get() +1)
        self.writeToFile(self.winFile, str(self.home1.get()))
        self.writeToFile(self.streakFile, str(self.streak.get()))
        self.streakCheck()

    def loseAction(self):
        self.away1.set(self.away1.get() + 1)

        self.awayScore.set(self.awayScore.get()+1) 
        
        self.totalGames.set(self.totalGames.get() + 1)
        self.streak.set(0)
        self.writeToFile(self.loseFile, str(self.away1.get()))
        self.writeToFile(self.streakFile, str(self.streak.get()))

    def drawAction(self):
        self.away1.set(self.away1.get() + 0.5)
        self.home1.set(self.home1.get()  + 0.5)

        self.homeScore.set(self.homeScore.get() +0.5)
        self.awayScore.set(self.awayScore.get() + 0.5)

                           
        self.totalGames.set(self.totalGames.get() + 1)
        self.streak.set(0)

        self.writeToFile(self.streakFile, str(self.streak.get()))
        self.writeToFile(self.loseFile, str(self.away1.get()))
        self.writeToFile(self.winFile, str(self.home1.get()))
        

  
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
