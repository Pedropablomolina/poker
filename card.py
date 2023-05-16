from comands import RANKS, SUITS


class Card:
    def __init__(self, suit, rank):
        if suit not in SUITS:
            raise ValueError(f"sorry, suit need to be one of : {SUITS}")
        if rank not in RANKS:
            raise ValueError(f"sorry, RANK need to be one of : {RANKS}")
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return



# ["♣","♦","♥","♠"]

c1 = Card("♥", "7")

print(c1)

try:
    c2 = Card("X","22")
    print(c2)
except ValueError:
    print("Unable to create Card")
c3 = Card("♥")