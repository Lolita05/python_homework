#Сгенерируйте 52-карточную колоду

import itertools as it


ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['H', 'D', 'C', 'S']

card_deck = it.product(ranks, suits)
print(list(card_deck))