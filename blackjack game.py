import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def getValue(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.value == 1:
                num_aces += 1
                value += 11
            elif card.value >= 10:
                value += 10
            else:
                value += card.value
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value

class Player:
    def __init__(self):
        self.hand = Hand()

    def drawCard(self, card):
        self.hand.addCard(card)

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def drawCard(self, card):
        self.hand.addCard(card)
    
    def showFirstCard(self):
        return self.hand.cards[0]
    
# Create the game
def playGame():
    deck = Deck()
    deck.shuffle()

    player = Player()
    dealer = Dealer()

    player.drawCard(deck.drawCard())
    player.drawCard(deck.drawCard())
    dealer.drawCard(deck.drawCard())
    dealer.drawCard(deck.drawCard())

    print(f"Your cards: {', '.join(str(card) for card in player.hand.cards)}")
    print(f"Dealer's first card: {dealer.showFirstCard()}")

    while player.hand.getValue() < 21:
        action = input("Do you want to hit or stand? ")
        if action.lower() == "hit":
            player.drawCard(deck.drawCard())
            print(f"Your cards: {', '.join(str(card) for card in player.hand.cards)}")
        else:
            break

    player_value = player.hand.getValue()

    while dealer.hand.getValue() < 17:
        dealer.drawCard(deck.drawCard())

    dealer_value = dealer.hand.getValue()

    print(f"Your cards: {', '.join(str(card) for card in player.hand.cards)}")
    print(f"Dealer's cards: {', '.join(str(card) for card in dealer.hand.cards)}")

    if player_value > 21:
        print("You bust, dealer wins!")
    elif dealer_value > 21:
        print("Dealer busts, you win!")
    elif player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

playGame()