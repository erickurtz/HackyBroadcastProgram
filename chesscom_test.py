import urllib.request
from bs4 import BeautifulSoup
import re
import tkinter as tk

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


class PlayerTracker:
    def __init__(self):
        self.opener = AppURLopener()
        self.data = []


    def getLatestGameFromURL(self, url):
        response = self.opener.open(url)
        soup = BeautifulSoup(response, 'html.parser')
        
        table = soup.find('table', attrs={'class':'table with-row-highlight table-archive'})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            self.data.append([ele for ele in cols if ele]) # Get rid of empty vals
            
        return self.parseGameFromString()

    def parseGameFromString(self):
        print ("parsing last game") 
        lastgame = str(self.data[0])
        lastgame = lastgame.replace('[', "")
        lastgame = lastgame.replace(']', "")
        lastgame = lastgame.replace("'", "")
        lastgame = lastgame.replace("\\n", " ")
        lastgame = lastgame.replace(",","")


        lastgame = re.sub(r" +", " ", lastgame)
        lastgame = re.sub(r" GM | IM | FM | NM | CM | WGM | WIM | WFM | WNM | WCM ", " ", lastgame)
        lastgame = re.sub(r"^(GM |IM |FM |NM |CM |WGM |WIM |WFM |WNM |WCM )", " ", lastgame)
        words = lastgame.split(" ")
        return words

## game list of of format
## ['natsky555', '(2583)', 'erichansen', '(2731)', '0', '1', '1', 'min', '23', 'Apr', '16', '2018']
## ['white-name', '(w-rate)', 'black-name', '(b-rate)

    
class ChessComMatchTracker:
    def __init__(self, master):
        self.winsFile = "homeScore.txt"
        self.lossesFile = "awayScore.txt"
        self.streakFile = "streak.txt"
        self.master = master
        self.start = False
        self.master.minsize(width=500,height=500)
        self.tracker = PlayerTracker()
        self.trackedUrl = ""
        self.latestGame = []
        self.previousGame = []        
        self.homeScore = Tk.DoubleVar()
        self.awayScore = Tk.DoubleVar()
        self.homeScore.set(0.0)
        self.awayScore.set(0.0)
        self.trackedPlayer = Tk.StringVar()
        self.opponentPlayer = Tk.StringVar()
        self.enterPlayer = Tk.Entry(self.master)
        self.trackedPlayer.set("")
        self.opponentPlayer.set("")
        self.startButton = Tk.Button(self.master, text = "Start", command = self.pressStart)
        self.inputName = Tk.Button(self.master, text = "Enter", command = self.setTrackerPlayer)
        
    def parseGame(self, game):
        print("nothing yet")
                                       
    def track(self):
        if self.start:
            print("started")
                       
    def pressStart(self):
        if(self.trackerPlayer.get() == ""):
            print("please enter a player") ##don't actually print anything
        else:
            self.start = not(self.start)
            if self.start:
                self.startButton["Stop"]
            else:
                self.startButton["Start"]
            
    def setTrackerPlayer(self):
        self.trackedPlayer = self.enterPlayer.get()
        self.trackedUrl = "https://www.chess.com/games/archive?username="+self.trackedPlayer
            
            
def main():
    url = "https://www.chess.com/games/archive?username=erichansen"
    parser = PlayerTracker()
    print (parser.getLatestGameFromURL(url))

main()
    
    
