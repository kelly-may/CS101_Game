# BlackJack
# game to demonstrate proficiency in CS101 from Codecademy
# written by Kelly May
# 04/14/2021

import random  # used to pick a random key from the dictionary

# deck_of_cards: { card name : [isAce? , value, isAvailable?] }

deck_of_cards = {"Ace of Clubs": [True, 11, True], "Two of Clubs": [False, 2, True], "Three of Clubs": [False, 3,True],
                 "Four of Clubs": [False, 4, True], "Five of Clubs": [False, 5, True],
                 "Six of Clubs": [False, 6, True], "Seven of Clubs": [False, 7, True] ,
                 "Eight of Clubs": [False, 8, True], "Nine of Clubs": [False, 9, True],
                 "Ten of Clubs": [False, 10, True], "Jack of Clubs": [False, 10, True],
                 "Queen of Clubs": [False, 10, True], "King of Clubs": [False, 10, True],

                 "Ace of Diamonds": [True, 11, True], "Two of Diamonds": [False, 2, True],
                 "Three of Diamonds": [False, 3, True], "Four of Diamonds": [False, 4, True],
                 "Five of Diamonds": [False, 5, True], "Six of Diamonds": [False, 6, True],
                 "Seven of Diamonds": [False, 7, True], "Eight of Diamonds": [False, 8, True],
                 "Nine of Diamonds": [False, 9, True], "Ten of Diamonds": [False, 10, True],
                 "Jack of Diamonds": [False, 10, True], "Queen of Diamonds": [False, 10, True],
                 "King of Diamonds": [False, 10, True],

                 "Ace of Hearts": [True, 11, True], "Two of Hearts": [False, 2, True],
                 "Three of Hearts": [False, 3, True], "Four of Hearts": [False, 4, True],
                 "Five of Hearts": [False, 5, True], "Six of Hearts": [False, 6, True],
                 "Seven of Hearts": [False, 7, True], "Eight of Hearts": [False, 8, True],
                 "Nine of Hearts": [False, 9, True], "Ten of Hearts": [False, 10, True],
                 "Jack of Hearts": [False, 10, True], "Queen of Hearts": [False, 10, True],
                 "King of Hearts": [False, 10, True],

                 "Ace of Spades": [True, 11, True], "Two of Spades": [False, 2,True],
                 "Three of Spades": [False, 3, True], "Four of Spades": [False, 4, True],
                 "Five of Spades": [False, 5, True], "Six of Spades": [False, 6, True],
                 "Seven of Spades": [False, 7, True], "Eight of Spades": [False, 8, True],
                 "Nine of Spades": [False, 9, True],  "Ten of Spades": [False, 10, True],
                 "Jack of Spades": [False, 10, True],  "Queen of Spades": [False, 10, True],
                 "King of Spades": [False, 10, True]
                 }


class Player:
    # class for defining each player (2 - 7 per game)
    # maxes number of players
    # assigns list of cards per player
    # calculates total value for each player
    card_list = []
    card_total = 0

    def __init__(self):
        pass





