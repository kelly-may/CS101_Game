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
    card_total = 0
    random1 = ""
    random2 = ""

    def __init__(self):
        # get 2 random cards that are available
        self.card_list = []  # cleared card list per new player
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
        self.card_total = 0
        for card in self.card_list:
            self.card_total += deck_of_cards[card][1]

        # run through cards again if over 21 to check for aces
        if self.card_total > 21:
            for card in self.card_list:
                if deck_of_cards[card][0] and self.card_total > 21:
                    self.card_total -= 10 # makes ace card worth 1 pt instead of 11
        return self.card_total

    def add_card(self):
        # adds another card to card_list
        random_card = random.choice(list(deck_of_cards.keys()))
        while not deck_of_cards[random_card][2]:
            random_card = random.choice(list(deck_of_cards.keys()))
        self.card_list.append(random_card)
        deck_of_cards[random_card][2] = False
        return self.card_list


print("Let's Play BlackJack!")
print("---------------------")
dealer = Player()
player_list = []
while True:
    try:
        num_players = int(input("How many players? (1-6): "))
    except Exception as e:
        print("please print a valid number.")
        continue
    if 1 < num_players > 6:
        print("please input a number 1-6: ")
        continue
    break

# makes a Player instance for each player
for num in range(num_players):
    player_list.append(Player())

# player's play one by one
for player in range(len(player_list)):
    print("----------------------------------------------")
    print("player " + str(player+1) + " your cards are: ")
    print(str(player_list[player].card_list))
    while True:
        try:
            hold_deal = input("(h)old or (d)eal another card?: ")
        except Exception as e:
            print("invalid entry.")
            continue
        if hold_deal == "d":
            player_list[player].add_card()
            print(str(player_list[player].card_list))
            continue
        elif hold_deal == "h":
            break

# now we deal the dealer's hands
print("----------------------------------------------")
print("The Dealer's hand is: ")
print(dealer.card_list)
while dealer.calculate_score() <= 17:
    dealer.add_card()
    print("dealer adds a card.")
    print(dealer.card_list)

print("dealer holds.")

# calculate scores
scores = []
for player in range(len(player_list)):
    score = player_list[player].calculate_score()
    if score > 21:
        scores.append(0)
        print("player " + str(player + 1) + " scored " + str(score) + " ...BUST!")
    else:
        scores.append(score)
        print("player " + str(player + 1) + " scored " + str(score))

# calculate dealer's score:
dealer_score = dealer.calculate_score()
if dealer_score > 21:
    print("dealer scored " + str(dealer_score) + "... BUST!")
    dealer_score = 0
else:
    print("dealer scored " + str(dealer_score))

# determine winner:
temp = 0
winner = 0
for points in range(len(scores)):
    if scores[points] > temp:
        winner = points  # assign winner
        temp = scores[points]  # use their score to compare next player
if temp <= dealer_score:
    winner = 7  # dealer wins

if winner == 7:
    print("dealer wins!")
else:
    print("player " + str(winner + 1) + " wins!")


















