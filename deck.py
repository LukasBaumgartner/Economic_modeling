class PlayingCard:
    SUITS = ["♦", "♣", "♥", "♠"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit, rank):
        # Check if the suit and rank are ok
        if suit not in self.SUITS:
            raise ValueError(f"suit must be in {self.SUITS}")
        if rank not in self.RANKS:
            raise ValueError(f"rank must be in {self.RANKS}")

        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank}{self.suit}"  # so I can print the card

    def __repr__(self):
        return self.__str__()


card = PlayingCard("♦", "7")
print(card.suit)
print(card.rank)
print(card)

card.rank = "A"  # cheater, we dont like cheaters (this will now fail)
print(card)