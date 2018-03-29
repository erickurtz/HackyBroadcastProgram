import Tkinter as Tk


class matchTrackerGUI:
    def __init__(self, master):
        self.file=open("output.txt", 'w+')
        self.file.write("")
        self.file.close()
        self.master = master
        master.title = "Simple Matchtracker"
        self.homeScore = 0.0
        self.totalGames = 0
        self.streak = 0
          
        self.winButton = Tk.Button(self.master, text = "Win", command = self.win)
        self.loseButton = Tk.Button(self.master, text = "Loss", command = self.loss)
        self.drawButton = Tk.Button(self.master, text = "Draw", command = self.draw)
        self.resetButton = Tk.Button(self.master, text = "Reset All", command = self.reset)
        self.resetStreakButton = Tk.Button(self.master, text = "Reset Streak",
                                  command = self.resetStreak)
        self.winButton.grid(row=1,column=1)
        self.loseButton.grid(row=2,column=1)
        self.drawButton.grid(row=3,column=1)
        self.resetButton.grid(row=1,column=2)
        self.resetStreakButton.grid(row=2,column=2)


    def getTheirScore(self):
        return totalGames - homeScore

    def writeToFile(self):
        file = open("output.txt",'w+')
        file.write("Streak: " + str(self.streak) + " games\n")
        if self.streak >= 10:
            file.write("Adoption.")
            file.close()
        return

    def resetStreak(self):
        file = open("output.txt", 'w+')
        file.write("")
        file.close()
        self.streak = 0
        return
    

    def reset(self):
        self.homeScore = 0.0
        self.totalGames = 0
        self.streak = 0
        file = open("output.txt", 'w+')
        file.write("")
        file.close()
        return
    
    def win(self):
        self.totalGames+=1
        self.homeScore+=1
        self.streak+=1
        self.writeToFile()
        return

    def loss(self):
        self.totalGames +=1
        self.resetStreak()
        return

    def draw(self):
        self.totalGames+= 0.5
        self.resetStreak()
        self.writeToFile()
        return 
  

def main():
    root = Tk.Tk()
    gui=matchTrackerGUI(root)
    root.mainloop()

main()
    



        

