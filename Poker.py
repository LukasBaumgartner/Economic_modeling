from deck import Deck

class PokerHand:
    def __init__(self):
        """
        Create a brand-new Deck, shuffle it and deal 5 cards!
        """
        deck = Deck() #Create a new deck
        deck.shuffle() #Shuffle the deck
        self._cards = [] #Create an empty hand
        for _ in range(5): #We deal 5 cards!
            self._cards.append(deck.deal()) # Add a card to the hand, until 5
    @property
    def cards(self):
        return tuple(self._cards)

    def __str__(self):
        return str(self.cards)

hand = PokerHand()
print(hand)

