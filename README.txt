CS101 Final Project for Codecademy
Build a CLI game - practice Python project
Requirements:
1. >= 1 interactive feature (input())
2. use Git
3. use command line and file navigation

Set-up:
1. using Pycharm with built-in Git version control

Idea:
1. Blackjack:
    a. create dictionary of 52 cards using: { card : value }
        i. Aces can be worth 1 or 11, so need if/else to decide value
        ii. face cards worth 10
        iii. pip values worth 2-10
    b. randomly assign the computer two cards and add their combined value
        i. if total value less than 17, add another random card
        ii. else, hold card value
    c. randomly assign user two cards and display their combined value
        i. if player has an Ace + 10 card value, automatically win (BlackJack)
        ii. Let player decide to pick another random card. If card makes total exceed 21, player loses (bust)
        iii. Let player decide to "hold"
    d. Total value of "dealer" cards vs player cards compared. Whoever is closer to 21 wins.
        i. if same value, tie.
