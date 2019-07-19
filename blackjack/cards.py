'''
Module for playing cards, with classes Card and Deck
Taken and edited from: https://github.com/georgemcredmond/BlackJackPython/blob/master/
Using under its MIT license

Author: George McRedmond

Card images were replaced with those from http://acbl.mybigcommerce.com/52-playing-cards/,
which were free to use for non-commercial purposes
'''
import random

'''A card object with a suit and rank.'''
class Card:

	RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

	SUITS = ("Spades", "Hearts", "Diamonds", "Clubs")

	BACK_NAME = "../PNG/BlueCardBack.png"

	'''Creates a card with the given rank and suit.'''
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		#rankName = ""
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
		self._filename = "../PNG/" + rankName + suit[0].lower() + ".png"
		self._faceup = False

	'''Resets the card's faceup attribute.'''
	def turn(self):
		self._faceup = not self._faceup

	'''Returns the card's image filename if it is face up or the backside filename if it is face down.'''
	def getFilename(self):
		if self._faceup:
			return self._filename
		else:
			return Card.BACK_NAME

	'''Returns the string representation of a card.'''
	def __str__(self):
		if self.rank == 1:
			rank = "Ace"
		elif self.rank == 11:
			rank = "Jack"
		elif self.rank == 12:
			rank = "Queen"
		elif self.rank == 13:
			rank = "King"
		else:
			rank = self.rank
		return str(rank) + " of " + self.suit

'''A deck containing 52 cards.'''
class Deck(object):

	'''Creates a full deck of cards.'''
	def __init__(self):
		self._cards = []
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				c = Card(rank, suit)
				self._cards.append(c)

	'''Shuffles the cards.'''
	def shuffle(self):
		random.shuffle(self._cards)

	'''Removes and returns the top card or None if the deck is empty.'''
	def deal(self):
		if len(self) == 0:
			return None
		else:
			return self._cards.pop(0)

	'''Returns the number of cards left in the deck.'''
	def __len__(self):
		return len(self._cards)

	'''Returns the string representation of a deck.'''
	def __str__(self):
		self.result = ''
		for c in self._cards:
			self.result = self.result + str(c) + '\n'
		return self.result
