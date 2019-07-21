'''
Taken and edited from: https://github.com/georgemcredmond/OichoKabuPython/blob/master/
Using under its MIT license
Author: George McRedmond

GUI based version of the OichoKabu card game
'''

from tkinter import *
from OichoKabu import OichoKabu
class OichoKabuGUI(Frame):

	def __init__(self):
		Frame.__init__(self)
		self._newGame()

	'''Instantiates the model and establishes the GUI'''
	def _newGame(self):
		self.destroy()
		Frame.__init__(self)
		self.master.title("Oicho Kabu")
		self.grid()

		#Add the command buttons
		self._hitButton = Button(self, text = "Hit", command = self._hit)
		self._hitButton.grid(row = 0, column = 0)

		self._passButton = Button(self, text = "Pass", command = self._pass)
		self._passButton.grid(row = 0, column = 1)

		self._newGameButton = Button(self, text = "New Game", command = self._newGame)
		self._newGameButton.grid(row = 0, column = 2)

		#Add the status field
		self._statusVar = StringVar()
		self._statusField = Entry(self, textvariable = self._statusVar)
		self._statusField.grid(row = 1, column = 0, columnspan = 3)

		#Add the panes for the player and dealer cards
		self._playerPane = Frame(self)
		self._playerPane.grid(row = 2, column = 0, columnspan = 3)
		self._dealerPane = Frame(self)
		self._dealerPane.grid(row = 3, column = 0, columnspan = 3)
		##
		self._model = OichoKabu()

		#Refresh the card panes
		#Player Cards
		self._playerImages = list(map(lambda card: getCardImage(card), self._model.getPlayerCards()))
		self._playerLabels = list(map(lambda i: Label(self._playerPane, image = i), self._playerImages))
		for col in range(len(self._playerLabels)):
			self._playerLabels[col].grid(row = 0, column = col)

		#Dealer Cards
		self._dealerImages = list(map(lambda card: getCardImage(card), self._model.getDealerCards()))
		self._dealerLabels = list(map(lambda i: Label(self._dealerPane, image = i), self._dealerImages))
		for col in range(len(self._dealerLabels)):
			self._dealerLabels[col].grid(row = 0, column = col)

		#Re-enable the buttons and clear the status field
		self._hitButton["state"] = NORMAL
		self._passButton["state"] = NORMAL
		self._statusVar.set("")

	'''Hits the player in the data model and updates its card pane. If the
	player points reach or exceed 21, hits the dealer too.'''
	def _hit(self):
		card = self._model.hitPlayer()
		cardImage = PhotoImage(file = card.getFilename())
		cardImage = cardImage.subsample(4, 4)
		self._playerImages.append(cardImage)
		label = Label(self._playerPane, image = cardImage)
		self._playerLabels.append(label)
		label.grid(row = 0, column = len(self._playerLabels) - 1)
		self._pass()   #Hits the dealer to finish

	'''Hits the dealer in the data model, updates its card pane, and displays
	the outcome of the game.'''
	def _pass(self):
		self._hitButton["state"] = DISABLED
		self._passButton["state"] = DISABLED

		#Hit dealer and refresh card pane
		self._model.hitDealer()
		self._dealerImages = list(map(lambda card: getCardImage(card), self._model.getDealerCards()))
		self._dealerLabels = list(map(lambda i: Label(self._dealerPane, image = i), self._dealerImages))
		for col in range(len(self._dealerLabels)):
			self._dealerLabels[col].grid(row = 0, column = col)
		playerRanks = []
		dealerRanks = []
		for card in self._model.getPlayerCards():
			playerRanks.append(card.rank)
		for card in self._model.getDealerCards():
			dealerRanks.append(card.rank)
		if(len(playerRanks) > 2):
			thirdPlayerCard = playerRanks[2]
		else:
			thirdPlayerCard = 0
		if(len(dealerRanks) > 2):
			thirdDealerCard = dealerRanks[2]
		else:
			thirdDealerCard = 0
		self._model.whoWins(playerRanks[0], playerRanks[1], thirdPlayerCard, dealerRanks[0], dealerRanks[1], thirdDealerCard)

def getCardImage(card):
	cardImage = PhotoImage(file = card.getFilename())
	cardImage = cardImage.subsample(4, 4)
	return cardImage

def main():
	OichoKabuGUI().mainloop()

main()
