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
    # passes deck of cards so can make cards unavailable for drawing.
    card_list = []

    def __init__(self):
        # get 2 random cards that are available
        self.random1 = random.choice(list(deck_of_cards.keys()))
        self.random2 = random.choice(list(deck_of_cards.keys()))
        # add random cards to player's card_list if available, and make unavailable
        while not deck_of_cards[self.random1][2]:
            self.random1 = random.choice(list(deck_of_cards.keys()))
        self.card_list.append(self.random1)
        deck_of_cards[self.random1][2] = False

        while not deck_of_cards[self.random2][2]:
            self.random2 = random.choice(list(deck_of_cards.keys()))
        self.card_list.append(self.random2)
        deck_of_cards[self.random2][2] = False

    def calculate_score(self):
        # calculates the score for a player based on the card_list
        card_total = 0
        for card in self.card_list:
            card_total += deck_of_cards[card][1]

        # run through cards again if over 21 to check for aces
        if card_total > 21:
            for card in self.card_list:
                if deck_of_cards[card][0] and card_total > 21:
                    card_total -= 10 # makes ace card worth 1 pt instead of 11
        return card_total

    def add_card(self):
        # adds another card to card_list
        random_card = random.choice(list(deck_of_cards.keys()))
        while not deck_of_cards[random_card][2]:
            random_card = random.choice(list(deck_of_cards.keys()))
        self.card_list.append(random_card)
        deck_of_cards[random_card]
        return self.card_list


player1 = Player()
print(deck_of_cards)
print(player1.card_list)
player1.add_card()
print(player1.card_list)
print(player1.calculate_score())


