import tkinter

global homeScore
global awayScore

homeScore = 0.0
awayScore = 0.0

def writeToFile(): 
	file = open("C:\\ourScore.txt", "w+")
	file.write(str(homeScore))
	file.close()
	file2 = open("C:\\theirScore.txt", "w+")
	file2.write(str(awayScore))
	file2.close()

def drawCallBack():
	global homeScore
	global awayScore
	homeScore += 0.5
	awayScore += 0.5 
	writeToFile()
	#open file, make draw 
def brahWinCallBack(): 
	global homeScore
	homeScore += 1
	writeToFile()
	
def theyWinCallBack():
	global awayScore
	awayScore += 1
	writeToFile()
	#increment their score by one
	
writeToFile()


top = tkinter.Tk()


win = tkinter.Button(top, text = "Win", command = brahWinCallBack)
loss = tkinter.Button(top, text = "Loss", command = theyWinCallBack)
draw = tkinter.Button(top, text = "Draw", command = drawCallBack)
win.pack()
loss.pack()
draw.pack()
top.mainloop() 