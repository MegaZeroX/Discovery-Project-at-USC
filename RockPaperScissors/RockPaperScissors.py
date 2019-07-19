'''The images are from company logo for Rock Paper Scissors Entertainment'''

from tkinter import *
import random
import RPS
'''Creates a GUI for Rock Paper Scissors'''
class RockPaperScissorsGUI(Frame):

    '''Creates the basic graphical layout'''
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Rock Paper Scissors")
        self.grid()
        self._rockImage = PhotoImage(file = r"../PNG/rock.png")
        self._rockLabel = Label(self, text="Rock", font=('Verdana', 15))
        self._rockButton = Button(self, text="roll", image=self._rockImage, command = lambda: self._shoot("rock"))
        self._rockLabel.grid(row = 0, column = 0)
        self._rockButton.grid(row = 1, column = 0)
        self._paperImage = PhotoImage(file = r"../PNG/paper.png")
        self._paperLabel = Label(self, text="Paper", font =('Verdana', 15))
        self._paperButton = Button(self, text="roll", image=self._paperImage, command = lambda: self._shoot("paper"))
        self._paperLabel.grid(row = 0, column = 1)
        self._paperButton.grid(row = 1, column = 1)
        self._scissorsImage = PhotoImage(file = r"../PNG/scissors.png")
        self._scissorsLabel = Label(self, text="Scissors", font =('Verdana', 15))
        self._scissorsButton = Button(self, text="roll", image=self._scissorsImage, command=lambda: self._shoot("scissors"))
        self._scissorsLabel.grid(row = 0, column = 2)
        self._scissorsButton.grid(row = 1, column = 2)

    '''Generates an opponents move, and asks student\'s code who won '''
    def _shoot(self, call):
        num = random.randint(0, 3)
        if(num == 1):
            RPS.rockPaperScissorsWinner(call, "rock")
        elif(num == 2):
            RPS.rockPaperScissorsWinner(call, "paper")
        else:
            RPS.rockPaperScissorsWinner(call, "scissors")

def main():
    RockPaperScissorsGUI().mainloop()

main()
