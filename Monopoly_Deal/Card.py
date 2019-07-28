class Card:
    """
    A Card from the card game Monopoly Deal, this is the superclass and should not be implemented as is
    ===Private Attributes===
    name: The card's name
    description: The card's description
    money_value: How much the card's money value is
    """
    name: str
    description: str
    money_value: int

    def __init__(self):
        self.name = ""
        self.description = ""
        self.money_value = 0

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_money_value(self):
        return self.money_value


class MoneyCard(Card):
    """
    A money card, only has the value of money to be stored in the bank
    """

    def __init__(self, money):
        self.money_value = money
        self.description = "This card has a money value of " + str(money) + \
                           ". You can put it in the bank and use it to pay people rent. "
        self.name = "$" + str(money) + " Million Money Card"

