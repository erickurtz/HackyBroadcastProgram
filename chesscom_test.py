

import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://www.chess.com/games/archive?username=erichansen"

def parse_game_data(game):
    return game.replace('\n', ' ')

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open(url)


soup = BeautifulSoup(response, 'html.parser')

data = []
table = soup.find('table', attrs={'class':'table with-row-highlight table-archive'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty vals



    
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
for word in words:
    print(word)
    
