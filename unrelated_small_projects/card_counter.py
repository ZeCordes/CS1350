from random import shuffle

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
RANK_MAP = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Jack, Queen, King are worth 10; Ace is worth 11

class Card:
    """Represents a playing card with a suit and rank."""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def value(self):
        """Returns the value of the card for counting purposes. (external handling needed for aces in blackjack)"""
        return RANK_MAP[RANKS.index(self.rank)]

def make_deck(num_decks=6):
    """Creates a deck of cards using the specified number of standard decks.

    Args:
        num_decks (int, optional): the number of standard decks (4 groups of each rank) to use. Defaults to 6.
    """
    deck = []
    for _ in range(num_decks):  # 4 suits per deck
        for suit in SUITS:
            for rank in RANKS:
                deck.append(Card(suit, rank))
    shuffle(deck)  # Shuffle the deck
        
    return deck

def hand_value(hand):
    """Calculates the total value of a hand of cards.

    Args:
        hand (list): A list of Card objects representing the hand.
    
    Returns:
        int: The total value of the hand.
    """
    total = 0
    aces = 0

    for card in hand:
        total += card.value()
        if card.rank == "Ace":
            aces += 1

    # Adjust for Aces
    while total > 21 and aces > 0:
        total -= 10  # Count Ace as 1 instead of 11
        aces -= 1

    return total

def display_hand(hand):
    """Displays the cards in a hand.

    Args:
        hand (list): A list of Card objects representing the hand.
    """
    print(f"Total value: {hand_value(hand)}\n")
    for card in hand:
        print(card)
    print("-" * 30)


def human_blackjack():
    """Simulates a simple game of Blackjack for a human player against a dealer with no other players."""
    deck = make_deck()
    playing = True
    stats = {"games": 0, "wins": 0, "losses": 0, "ties": 0}
    
    while playing:
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print("Your hand:")
        display_hand(player_hand)
        
        print("Dealer's hand:")
        print(dealer_hand[0])
        print("Hidden card\n" + "-" * 30)
        
        while True:
            action = input("Do you want to (h)it or (s)tand? ").lower()
            if action in ['h', 'hit']:
                player_hand.append(deck.pop())
                print("Your hand:")
                display_hand(player_hand)
                if hand_value(player_hand) > 21:
                    print("You busted! Dealer wins.")
                    break
            elif action in ['s', 'stand']:
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")
        
        stats["games"] += 1
        if hand_value(player_hand) <= 21:
            while hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
            print("Dealer's hand:")
            display_hand(dealer_hand)
            if hand_value(dealer_hand) > 21:
                print("Dealer busted! You win.")
                stats["wins"] += 1
            elif hand_value(dealer_hand) > hand_value(player_hand):
                print("Dealer wins.")
                stats["losses"] += 1
            elif hand_value(dealer_hand) < hand_value(player_hand):
                print("You win!")
                stats["wins"] += 1
            else:
                print("It's a tie!")
                stats["ties"] += 1
        else:
            display_hand(dealer_hand)
            print("You busted! Dealer wins.")
            stats["losses"] += 1
            
        again = input("Do you want to play again? (y/n) ").lower()
        if again not in ['y', 'yes', '']: # empty string to keep gambling
            playing = False
            print("Thanks for playing!")
    
    print("\nGame statistics:")
    print(f"Total games played: {stats['games']}")
    print(f"Total wins: {stats['wins']}")
    print(f"Total losses: {stats['losses']}")
    print(f"Total ties: {stats['ties']}")
    
    print(f"Final win rate: {stats['wins'] / stats['games'] * 100:.2f}%")
    print(f"Money made (assuming $1 per game): ${stats['wins'] - stats['losses']}")


if __name__ == "__main__":
    human_blackjack() # TODO: add bot players with different strategies, also money