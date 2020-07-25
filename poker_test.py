from enum import Enum

class Suit(Enum):
  Spade=4
  Heart=3
  Diamond=2
  Club=1

class Card:
  def __init__(self, number: int, suit: Suit):
    self.number = number
    self.suit = suit

  def __str__(self):
    if self.suit == Suit.Spade.value:
      sign = '\u2660'
    elif self.suit == Suit.Heart.value:
      sign = '\u2661'
    elif self.suit == Suit.Diamond.value:
      sign = '\u2662'
    else:
      sign = '\u2663'
    return f"{sign} {self.number}"

card1 = Card(9, 4)
print(card1)


# your exercise, randomely generate 2 cards, display the 2 cards, and compare them
