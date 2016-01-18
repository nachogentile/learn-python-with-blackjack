"""Object-Oriented version of Blackjack game"""
from random import random


class Player:
    """A player of Blackjack"""
    def __init__(self):
        self.name = raw_input('Player, say your name: ')
        self.score = 0

    def get_score(self):
        return "%s score is %d" % [self.name, self.score]


class Deck:
    """A deck for playing blackjack"""
    def __init__(self):
        self.cards = []
        for colour in Blackjack.card_colours:
            for card in Blackjack.card_values:
                self.cards.append(Card(card, colour))

    def get_random_card(self):
        position = int(random() * len(self.cards))
        selected_card = self.cards[position]
        del self.cards[position]
        return selected_card


class Card:
    """A card for playing blackjack"""
    def __init__(self, number, colour):
        self.number = number
        self.colour = colour

    def get_value(self, total):
        if total >= 11 and self.number == 'A':
            return 1
        return Blackjack.card_values[self.number]

    def __str__(self):
        return self.number + " of " + self.colour


class Blackjack:
    """Main class for blackjack game """

    def __init__(self):
        # We'll define 2 players, FIXME: you can try to modify it to admit as many players as desired
        self.players = [Player(), Player()]
        # The deck is generated, FIXME: allow the user to choose the amount of decks he wants to play with
        self.deck = Deck()

    # Values of cards for the game, used to count the score
    card_values = {
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

    # Card colours
    card_colours = ["diamonds", "heart", "spades", "clubs"]

    def play(self):
        max_score = 0
        winner = None

        for player in self.players:
            table_cards = []
            user_input = 'y'
            while user_input == 'y':
                # Give card
                card = self.deck.get_random_card()
                print card
                table_cards.append(card)
                # Check if you lost
                if self.calculate_score(table_cards) >= 21:
                    break
                user_input = raw_input('Do you want another card? (Y)')
            print "Your score is: %d" % self.calculate_score(table_cards)
            player.score = (self.calculate_score(table_cards))

            if 21 >= player.score > max_score:
                winner = player
                max_score = player.score

        # FIXME: What would happen if every one score is above 21? Prevent it!
        print winner.get_score()

    def calculate_score(self, card_list):
        total = 0
        for card in card_list:
            total += card.get_value(total)
        return total


def main():
    game = Blackjack()
    game.play()


if __name__ == "__main__":
    main()
