'''
Taken and edited from: https://github.com/georgemcredmond/BlackJackPython/blob/master/
Using under its MIT license
Author: George McRedmond

Establishes a player class, dealer class, and game mechanics for a BlackJack card game.
'''

from cards import Deck, Card
import BJ
'''This class represents a player in a blackjack game.'''
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
			elif(card.rank == 11):
				cardName += "J"
			elif(card.rank == 12):
				cardName += "Q"
			elif(card.rank == 13):
				cardName += "K"
			else:
				cardName += str(card.rank)
			cardList.append(cardName)
		return BJ.calculatePoints(cardList)

	'''Dealt 21 or not'''
	def hasBlackjack(self):
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

	'''Add cards while points < 17, then allow all to be shown.'''
	def hit(self, deck):
		while self.getPoints() < 17:
			card = deck.deal()
			card.turn()
			self._cards.append(card)

	'''Turns over the first card to show it'''
	def turnFirstCard(self):
		self._showOneCard = False
		self._cards[0].turn()

class Blackjack(object):

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
		return (card, self._player.getPoints())

	'''Deals cards to the dealer until an outcome occurs. Returns a string representing the outcome.'''
	def hitDealer(self):
		self._dealer.turnFirstCard()
		playerPoints = self._player.getPoints()
		if playerPoints > 21:
			return "You bust and lose!"
		else:
			self._dealer.hit(self._deck)
			dealerPoints = self._dealer.getPoints()
			if dealerPoints > 21:
				return "Dealer busts, you win!"
			elif dealerPoints > playerPoints:
				return "Dealer wins :("
			elif dealerPoints < playerPoints and playerPoints <= 21:
				return "Congrats! You win!"
			elif dealerPoints == playerPoints:
				if self._player.hasBlackjack() and not self._dealer.hasBlackjack():
					return "Blackjack! You Win!"
				elif not self._player.hasBlackjack() and self._dealer.hasBlackjack():
					return "Dealer Blackjack! You lose!"
				else:
					return "There is a tie"
