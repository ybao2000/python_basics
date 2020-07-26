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

    if self.number == 11:
      point = "J"
    elif self.number == 12:
      point = "Q"
    elif self.number ==  13:
      point = "K"
    elif self.number == 1:
      point = "A"
    else:
      point = str(self.number)
    return sign + ' ' + point

# card1 = Card(9, 4)
# print(card1)


# your exercise, randomely generate 2 cards, display the 2 cards, and compare them
import random
card1 = Card(random.randint(1, 13), random.randint(1, 4))
card2 = Card(random.randint(1, 13), random.randint(1, 4))
print(f"Card 1: {card1}")
print(f"Card 2: {card2}")

if card1.number == 1:
  if card2.number != 1:
    compare = True
  else:
    compare = card1.suit >= card2.suit
elif card2.number == 1:
  if card1.number != 1:
    compare = False
  else:
    compare = card1.suit >= card2.suit
else:
  if card1.number == card2.number:
    compare = card1.suit >= card2.suit
  else:
    compare = card1.number >= card2.number

# ternary operator 
answer = "Card 1 Wins!" if compare else "Card 2 wins!"

print(answer)