from Deck import Deck


class Player:
    """
    A player class to initiate a player.
    === Attributes ===
    cards: The cards in this players hand.
    """
    cards: Deck

    def __init__(self, deck: Deck):
        self.cards = Deck()
        for i in range(5):
            self.cards.add(deck.draw())
