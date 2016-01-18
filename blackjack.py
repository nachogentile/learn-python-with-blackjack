"""Blackjack game to teach a friend python basics."""

# This is how to import a module in python, in this case I import the random module, included in the standard library
from random import random

# This is a list, I use a list to store the available card colours
card_colours = ["diamonds", "heart", "spades", "clubs"]

# This is a dictionary definition, I will use it to match the number or name of the card with its value inside the game
card_value = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

# This is a function, this function contains a docstring, which defines the scope of the function, its arguments
# and return values

def calculate_score(card_list):
    """Calculate the score based on a list of cards

    Args:
        card_list: list of cards
    Returns:
        total score of the list of cards
    """
    total = 0
    for card in card_list:
        # Normally 'A' card is 11 points, but user can decide in case the sum of the score is above 21, to count
        # 'A' as 1 instead of 11, so if we find an ace and we are at 11 or more score, it will count as 1 point.
        if total >= 11 and card == 'A':
            total += 1
        else:
            total += card_value[card]
    return total


def play_turn(deck):
    """Run a turn of Blackjack for a player

    Args:
        deck: list of cards available
    Returns:
        total score of the turn
    """
    # We will store all the cards that come out in the following list
    table_cards = []
    user_input = 'y'
    # While user says 'y' and the player haven't lost, cards will come out
    while user_input == 'y':
        # Calculate random card position
        position = int(random() * len(deck))
        # Give card
        print deck[position]
        table_cards.append(deck[position][0])
        del deck[position]
        # Check if you lost, if you did the cycle will break
        if calculate_score(table_cards) >= 21:
            break
        # We ask the user through raw_input function if he want another card
        user_input = raw_input('Do you want another card? (Y)')
    print "Your score is: %d" % calculate_score(table_cards)
    # Return the round total score
    return calculate_score(table_cards)


# I created a 'main' function in order to place the main execution code of our game, it's called every time the
# program starts.

def main():
    # Define an empty deck
    deck = []
    # Populate the deck with all the 52 cards
    # For each colour...
    for colour in card_colours:
        # And for each card
        for card in card_value:
            # Append a card-colour couple in form of a tuple, the deck will look like this:
            # [('A', 'diamonds'), ('2', 'diamonds'), ('3', 'diamonds')...]
            deck.append((card, colour))

    # Create a list of players, in this case 2 players will play
    players = ['player 1', 'player 2']

    max_score = 0
    winner = None

    # I will run the game one time per player
    for player in players:
        print "\n%s, your turn starts now!\n" % player
        score = play_turn(deck)
        # We check who is winning the match, if the current player score is above previous highest,
        # he is the new winner
        if 21 >= score > max_score:
            max_score = score
            winner = player

    print "Winner is %s" % winner


if __name__ == "__main__":
    main()