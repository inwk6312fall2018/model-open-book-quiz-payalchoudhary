import pyCardDeck
from pyCardDeck.cards import PokerCard

class Player:

	def __init__(self,name):
		self.name = str(name)

	def __str__(self):
		return self.name

class PokerTable:
	
	def __init__(self, players):
		self.players = list(range(1,players))
		self.deck = pyCardDeck.Deck(cards=generate_initial_deck(),name='Poker Game',reshuffle=False)
		self.table_cards=[]
		self.hand = []
		print("This is a poker table with {} players".format(players))


	def texas_holdem(self):
		"""Basic Texas Hold'em game structure"""
		print("Starting a round of Texas Hold'em")
		self.deck.shuffle()
		self.draw_cards(2)
		
	def draw_cards(self, number):
		card = []
		for _ in range(0, number):
			for player in self.players:
				card = self.deck.draw()
				player.append(card)
			print("Dealt {} to player {}".format(card, player))

def generate_initial_deck():
		cards=[]
		suit = ["Hearts","Spades","Clubs","Diamonds"]
		ranks= {'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','J':'Jack','Q':'Queen','K':'King'}

		for item in suit:
			for rank,name in ranks.items():
				cards.append((item,name))
		print('Generated deck of cards for the table')
		return cards

PT = PokerTable(5)
print(generate_initial_deck())
print(PT.draw_cards(5))

