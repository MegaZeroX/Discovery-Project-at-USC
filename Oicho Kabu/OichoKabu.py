'''
Taken and edited from: https://github.com/georgemcredmond/BlackJackPython/blob/master/
Using under its MIT license
Author: George McRedmond

Establishes a player class, dealer class, and game mechanics for a Oicho Kabu card game.
'''

from cards import Deck, Card
import OK
'''This class represents a player in a OichoKabu game.'''
class Player(object):
	def __init__(self, cards):
		self._cards = cards
		for card in self._cards:
			card.turn()

	'''Returns string rep of cards and points.'''
	def __str__(self):
		result = ", ".join(map(str, self._cards))
		result += "\n  " + str(self.getPoints()) + " points"
		return result

	def hit(self, card):
		self._cards.append(card)

	'''Translates cards into a list and asks students to calculate the points'''
	def getPoints(self):
		count = 0
		cardList = []
		for card in self._cards:
			cardName = card.suit[0]
			if(card.rank == 1):
				cardName += "A"
			elif(card.rank == 10):
				cardName += "T"
			else:
				cardName += str(card.rank)
			cardList.append(cardName)
		return BJ.calculatePoints(cardList)

	'''Dealt 21 or not'''
	def hasOichoKabu(self):
		return len(self._cards) == 2 and self.getPoints() == 21

	def getCards(self):
		return self._cards

'''Like a player, but with some restrictions'''
class Dealer(Player):

	'''Initial state: show one card only'''
	def __init__(self, cards):
		Player.__init__(self, cards)
		self._showOneCard = True
		self._cards[0].turn()

	'''Return just one card if not hit yet.'''
	def __str__(self):
		if self._showOneCard:
			return str(self._cards[0])
		else:
			return Player.__str__(self)

	'''Give a dealer a card.'''
	def hit(self, card):
		self._cards.append(card)

	'''Turns over the first card to show it'''
	def turnFirstCard(self):
		self._showOneCard = False
		self._cards[0].turn()

class OichoKabu(object):

	def __init__(self):
		self._deck = Deck()
		self._deck.shuffle()

		#Pass the player and the dealer two cards each
		self._player = Player([self._deck.deal(), self._deck.deal()])
		self._dealer = Dealer([self._deck.deal(), self._deck.deal()])

	'''Returns a list of the player's cards.'''
	def getPlayerCards(self):
		return self._player.getCards()

	'''Returns a list of the dealer's cards.'''
	def getDealerCards(self):
		return self._dealer.getCards()

	'''Deals a card to the player. Returns a tuple of the card and the player's points.'''
	def hitPlayer(self):
		card = self._deck.deal()
		card.turn()
		self._player.hit(card)
		return card

	'''Deals cards to the dealer until an outcome occurs. Returns a string representing the outcome.'''
	def hitDealer(self):
		card = self._deck.deal()
		card.turn()
		sum = self._dealer._cards[0].rank + self._dealer._cards[1].rank
		if(sum % 10 < 6):
			self._dealer.hit(card)
		self._dealer.turnFirstCard()

	def whoWins(self, playerCardOne, playerCardTwo, playerCardThree, dealerCardOne, delearCardTwo, dealerCardThree):
		OK.whoWins(playerCardOne, playerCardTwo, playerCardThree, dealerCardOne, delearCardTwo, dealerCardThree)
