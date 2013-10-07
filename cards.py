import random as rand

class Deck:
    def __init__(self):
        ranks = ['A','2','3','4','5','6','7',
                 '8','9','10','J','Q','K']
        suits = ['C','D','H','S']
        self.deck = [Card(s,r) for s in suits for r in ranks]
        rand.shuffle(self.deck)

    def hand(self, n=1):
        """Deal n cards.  Return hand as list."""
        hand = [self.deck[i] for i in range(n)]
        del self.deck[:n]
        return hand

    def deal(self, cards_per_hand, num_players):
        """Deal num_of_players hands.  Returns list of lists, each
        sub-list being a player's hand."""
        return [self.hand(cards_per_hand) for i in range(num_players)]

    def putback(self, card):
        """Put card back under the rest."""
        self.deck.append(card)

    def __str__(self):
        return str(self.deck)

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.deck)


class Card:
    """Representation of a card as a string (suit+rank)."""
    def __init__(self, suit, rank):
        self.card = suit + str(rank)

    def __str__(self):      return self.card
    def __repr__(self):     return str(self)


class Hand:
    """Representation of a hand as a list of Card objects."""
    def __init__(self, list_of_cards):
        self.hand = list_of_cards
    def __str__(self):      return str(self.hand)
    def __repr__(self):     return str(self)
