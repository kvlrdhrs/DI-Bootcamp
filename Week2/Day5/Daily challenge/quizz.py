import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
        self.shuffle()

    def shuffle(self):
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return "No more cards in the deck"

# Example usage
deck = Deck()
print("Shuffled deck:")
print(deck.cards)

print("\nDealing cards:")
print(deck.deal())
print(deck.deal())
print(deck.deal())

print("\nRemaining cards in deck:")
print(deck.cards)