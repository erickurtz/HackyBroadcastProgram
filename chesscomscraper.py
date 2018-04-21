import urllib.request
from bs4 import BeautifulSoup
import re

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

class PlayerTracker:
    def __init__(self):
        self.opener = AppURLopener()
        self.data = []


    def getLatestGameFromURL(self, url):
        data2 = []
        response = self.opener.open(url)
        soup = BeautifulSoup(response, 'html.parser')
        
        table = soup.find('table', attrs={'class':'table with-row-highlight table-archive'})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data2.append([ele for ele in cols if ele]) # Get rid of empty vals
        self.data = data2
        self.opener.close()    
        return self.parseGameFromString()

    def parseGameFromString(self):
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
        if words[0] == '':
            words = words[1:]

        words[1] = words[1][1:-1]
        words[3] = words[3][1:-1]
        words[9] =  words[9] + " " + words[10] + " " + words[11] 
        words = words[:-2]
        words[6] = words[6] + " " + words[7]
        words = words[:7] + words [8:]
        return words

## game list of of format
## ['natsky555', '(2583)', 'erichansen', '(2731)', '0', '1', '1', 'min', '23', 'Apr', '16', '2018']
## ['white-name', '(w-rate)', 'black-name', '(b-rate)
