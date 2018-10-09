import pyCardDeck
from pyCardDeck.cards import PokerCard

def generate_initial_deck():
	cards=[]
	suit = ["Hearts","Spades","Clubs","Diamonds"]
	ranks= {'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','J':'Jack','Q':'Queen','K':'King'}

	for item in suit:
		for rank,name in ranks.items():
			cards.append((item,name))
	print('Generated deck of cards for the table')
	return cards
deck = generate_initial_deck()
print(deck)
