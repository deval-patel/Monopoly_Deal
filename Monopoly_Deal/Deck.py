import math
import random
import typing
from Card import *
from collections import deque
"""
This class holds a set of cards as a Deck.  
"""


class Deck:
    """
    ===Private Attributes===
    cards:
            The cards in this deck at this time.
    """
    cards: deque[Card]

    def __init__(self) -> None:
        self.cards = deque()

    def shuffle(self) -> None:
        for i in range(1000):
            num1 = random.randint(0, len(self.cards))
            num2 = random.randint(0, len(self.cards))
            self.cards[num1], self.cards[num2] = self.cards[num2], self.cards[num1]

    def draw(self) -> Card:
        return self.cards.pop()

    # TODO: Make generate method which initializes the Deck for the first time.
    def generate(self) -> None:
        pass

    def add(self, item: Card):
        self.cards.append(item)




