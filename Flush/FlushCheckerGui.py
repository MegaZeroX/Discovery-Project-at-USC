from tkinter import *
import cards
from FC import isFlush
class FlushCheckerGUI(Frame):

	def __init__(self):
		Frame.__init__(self)
		self._clear()

	'''Instantiates the model and establishes the GUI'''
	def _clear(self):
		self.destroy()
		Frame.__init__(self)
		self.master.title("FlushChecker")
		self.grid()

		#Add the command buttons
		self._flushButton = Button(self, text = "Draw a Flush", command = self._flush)
		self._flushButton.grid(row = 0, column = 0)

		self._randomButton = Button(self, text = "Draw Randomly", command = self._random)
		self._randomButton.grid(row = 0, column = 1)

		self._clearButton = Button(self, text = "Clear", command = self._clear)
		self._clearButton.grid(row = 0, column = 2)

		#Add the status field
		self._statusVar = StringVar()
		self._statusField = Entry(self, textvariable = self._statusVar)
		self._statusField.grid(row = 1, column = 0, columnspan = 3)

		#Add the panes for the player and dealer cards
		self._cardPane = Frame(self)
		self._cardPane.grid(row = 2, column = 0, columnspan = 3)

		#Re-enable the buttons and clear the status field
		self._flushButton["state"] = NORMAL
		self._randomButton["state"] = NORMAL
		self._statusVar.set("")

	'''Hits the player in the data model and updates its card pane. If the
	player points reach or exceed 21, hits the dealer too.'''
	def _flush(self):
		self._flushButton["state"] = DISABLED
		self._randomButton["state"] = DISABLED
		deck = cards.Deck()
		deck.shuffle()
		cardObjList = deck.dealFlush()
		#Hit dealer and refresh card pane
		self._cardImages = list(map(lambda card: getCardImage(card), cardObjList))
		self._cardLabels = list(map(lambda i: Label(self._cardPane, image = i), self._cardImages))
		for col in range(len(self._cardLabels)):
			self._cardLabels[col].grid(row = 0, column = col)
		cardNames = transform(cardObjList)
		if(isFlush(cardNames)):
			self._statusVar.set("It is a flush")
		else:
			self._statusVar.set("It is NOT a flush")

	'''Hits the dealer in the data model, updates its card pane, and displays
	the outcome of the game.'''
	def _random(self):
		self._flushButton["state"] = DISABLED
		self._randomButton["state"] = DISABLED
		deck = cards.Deck()
		deck.shuffle()
		cardObjList = []
		for i in range(5):
			cardObjList.append(deck.deal())
		#Hit dealer and refresh card pane
		self._cardImages = list(map(lambda card: getCardImage(card), cardObjList))
		self._cardLabels = list(map(lambda i: Label(self._cardPane, image = i), self._cardImages))
		for col in range(len(self._cardLabels)):
			self._cardLabels[col].grid(row = 0, column = col)
		cardNames = transform(cardObjList)
		if(isFlush(cardNames)):
			self._statusVar.set("It is a flush")
		else:
			self._statusVar.set("It is NOT a flush")

def getCardImage(card):
	cardImage = PhotoImage(file = card.getFilename())
	cardImage = cardImage.subsample(4, 4)
	return cardImage

def transform(cardList):
	formatted = []
	for card in cardList:
		name = card.suit[0]
		rank = card.rank
		if(rank == 1):
			rankName = "A"
		elif(rank == 10):
			rankName = "T"
		elif(rank == 11):
			rankName = "J"
		elif(rank == 12):
			rankName = "Q"
		elif(rank == 13):
			rankName = "K"
		else:
			rankName = str(rank)
		name += rankName
		formatted.append(name)
	return formatted


def main():
	FlushCheckerGUI().mainloop()

main()
