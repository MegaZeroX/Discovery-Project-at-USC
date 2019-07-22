from tkinter import *
from dice import *
from CeeLo import *

class CeeLoGui(Frame):
    def __init__(self):
        Frame.__init__(self)
        self._newGame()

    def _newGame(self):
        self.destroy()
        Frame.__init__(self)
        self.master.title("Cee-lo")
        self.grid()
        self._game = CeeLo()

        self._rollAllButton = Button(self, text = "Roll All Dice", command = self._rollAll)
        self._rollAllButton.grid(row = 0, column = 0)

        self._rerollFirstButton = Button(self, text = "Reroll first die", command = lambda: self._reroll(0))
        self._rerollFirstButton.grid(row = 0, column = 1)

        self._rerollSecondButton = Button(self, text = "Reroll second die", command = lambda: self._reroll(1))
        self._rerollSecondButton.grid(row = 0, column = 2)

        self._rerollThirdButton = Button(self, text = "Reroll third die", command = lambda: self._reroll(2))
        self._rerollThirdButton.grid(row = 0, column = 3)

        self._passButton = Button(self, text = "Keep Hand", command = self._pass)
        self._passButton.grid(row = 0, column = 4)

        self._newGameButton = Button(self, text = "New Game", command = self._newGame)
        self._newGameButton.grid(row = 0, column = 5)

        #Add the field to display number of remaining rolls
        self._statusVar = StringVar()
        self._statusField = Entry(self, textvariable = self._statusVar)
        self._statusField.grid(row = 1, column = 0, columnspan = 3)

        #Pane for dice to be displayed
        self._playerDicePane = Frame(self)
        self._playerDicePane.grid(row = 2, column = 0, columnspan = 3)

        self._opponentDicePane = Frame(self)
        self._opponentDicePane.grid(row = 3, column = 0, columnspan = 3)

        #Re-enable the buttons and clear the status field
        self._rollAllButton["state"] = NORMAL
        self._rerollFirstButton["state"] = DISABLED
        self._rerollSecondButton["state"] = DISABLED
        self._rerollThirdButton["state"] = DISABLED
        self._passButton["state"] = NORMAL
        self._statusVar.set("3 rolls remaining")

    def _rollAll(self):
        self._game.roll_all()
        self._playerDicePane = Frame(self)
        self._playerDicePane.grid(row = 2, column = 0, columnspan = 3)
        self._playerDiceImages = list(map(lambda dieRoll: getDiceImage(dieRoll), self._game.current_rolls()))
        self._playerDiceLabels = list(map(lambda i: Label(self._playerDicePane, image = i), self._playerDiceImages))
        for col in range(len(self._playerDiceLabels)):
            self._playerDiceLabels[col].grid(row = 0, column = col)
        self._statusVar.set(str(self._game.get_player_rolls_remaining()) + " rolls remaining")
        if(self._game.get_player_rolls_remaining() == 2):
            self._rerollFirstButton["state"] = NORMAL
            self._rerollSecondButton["state"] = NORMAL
            self._rerollThirdButton["state"] = NORMAL
        if(self._game.get_player_rolls_remaining() == 1):
            self._rerollFirstButton["state"] = DISABLED
            self._rerollSecondButton["state"] = DISABLED
            self._rerollThirdButton["state"] = DISABLED
        if(self._game.get_player_rolls_remaining() == 0):
            self._pass()

    def _reroll(self, index):
        self._game.reroll(index)
        self._playerDicePane = Frame(self)
        self._playerDicePane.grid(row = 2, column = 0, columnspan = 3)
        self._playerDiceImages = list(map(lambda dieRoll: getDiceImage(dieRoll), self._game.current_rolls()))
        self._playerDiceLabels = list(map(lambda i: Label(self._playerDicePane, image = i), self._playerDiceImages))
        for col in range(len(self._playerDiceLabels)):
            self._playerDiceLabels[col].grid(row = 0, column = col)
        self._statusVar.set(str(self._game.get_player_rolls_remaining()) + " rolls remaining")
        if(self._game.get_player_rolls_remaining() == 1):
            self._rerollFirstButton["state"] = DISABLED
            self._rerollSecondButton["state"] = DISABLED
            self._rerollThirdButton["state"] = DISABLED
        if(self._game.get_player_rolls_remaining() == 0):
            self._pass()

    def _pass(self):
        self._rollAllButton["state"] = DISABLED
        self._rerollFirstButton["state"] = DISABLED
        self._rerollSecondButton["state"] = DISABLED
        self._rerollThirdButton["state"] = DISABLED
        self._passButton["state"] = DISABLED

        self._game.roll_opponent()

        self._opponentDiceImages = list(map(lambda dieRoll: getDiceImage(dieRoll), self._game.opponent_roll()))
        self._opponentDiceLabels = list(map(lambda i: Label(self._opponentDicePane, image = i), self._opponentDiceImages))
        for col in range(len(self._opponentDiceLabels)):
            self._opponentDiceLabels[col].grid(row = 0, column = col)
        player_score, opponent_score = self._game.final_score()
        if(player_score > opponent_score):
            self._statusVar.set("You win!")
        else:
            self._statusVar.set("You lose!")

def getDiceImage(dieRoll):
    file_name = "die" + str(dieRoll) + ".png"
    file_path = "../PNG/" + file_name
    die_image = PhotoImage(file = file_path)
    return die_image

def main():
    CeeLoGui().mainloop()

main()
