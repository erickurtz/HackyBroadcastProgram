import urllib.request
from bs4 import BeautifulSoup
import re





class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


class PlayerTracker:
    def __init__(self, url):
        self.opener = AppURLopener()
        data = []


    def getLatestGameFromURL(self, url):
        response = self.opener.open(url)
        soup = BeautifulSoup(response, 'html.parser')
        
        table = soup.find('table', attrs={'class':'table with-row-highlight table-archive'})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele]) # Get rid of empty vals
            
        return self.parseGameFromString()

    def parseGameFromString():
        lastgame = str(data[0])
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
    
def __main__():
    url = "https://www.chess.com/games/archive?username=erichansen"
    parser = PlayerTracker(url)
    
    
