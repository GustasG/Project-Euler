import collections
from enum import Enum, auto
from dataclasses import dataclass

from shared.paths import RESOURCE_DIR


class Rank(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return not(self > other)

    def __ge__(self, other):
        return not(self < other)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not(self == other)


class Winner(Enum):
    Player1 = auto()
    Player2 = auto()
    NONE = auto()


@dataclass(frozen=True)
class Card:
    CARD_VALUES = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    value: str
    suit: str

    def evaluate(self) -> int:
        return Card.CARD_VALUES[self.value]


class Hand:
    HAND_CARD_COUNT = 5

    def __init__(self, cards: list[Card]):
        assert(len(cards) == Hand.HAND_CARD_COUNT)

        self.cards = cards
        self.card_values = sorted((card.evaluate() for card in self.cards), reverse=True)
        self.rank = Rank.HIGH_CARD

        count = collections.Counter(self.card_values)
        most_common, second_most_common = count.most_common(2)
        self.most_common_value, most_common_count = most_common
        self.second_most_common_value, second_most_common_count = second_most_common

        if most_common_count == 4:
            self.rank = Rank.FOUR_OF_KIND  # Four cards of same value
        elif most_common_count == 3:
            if second_most_common_count == 2:
                self.rank = Rank.FULL_HOUSE  # Tree of a kind and a pair
            else:
                self.rank = Rank.THREE_OF_KIND
        elif most_common_count == 2:
            if second_most_common_count == 2:
                self.rank = Rank.TWO_PAIRS  # Two different pairs
            else:
                self.rank = Rank.ONE_PAIR  # One pair
        else:
            is_flush = len(set(card.suit for card in self.cards)) == 1
            is_straight = (self.card_values[0] - self.card_values[-1]) == Hand.HAND_CARD_COUNT - 1

            if is_straight:
                if is_flush:
                    self.rank = Rank.STRAIGHT_FLUSH  # All cards consecutive and same suit
                else:
                    self.rank = Rank.STRAIGHT  # All cards are consecutive
            else:
                if is_flush:
                    self.rank = Rank.FLUSH  # All cards of the same suit

    def __str__(self):
        return ''.join(f'{card} ' for card in self.cards)

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.cards)})'


def read_file(path) -> tuple[list[Hand], list[Hand]]:
    with open(path, 'r') as f:
        first_player_cards = []
        second_player_cards = []

        for line in f:
            cards = line.split()

            first_player_cards.append(Hand([Card(*card) for card in cards[0:5]]))
            second_player_cards.append(Hand([Card(*card) for card in cards[5:10]]))

        return first_player_cards, second_player_cards


def find_winner(first_hand: Hand, second_hand: Hand) -> Winner:
    if first_hand.rank < second_hand.rank:
        return Winner.Player2
    elif first_hand.rank > second_hand.rank:
        return Winner.Player1
    else:
        if first_hand.most_common_value < second_hand.most_common_value:
            return Winner.Player2
        elif first_hand.most_common_value > second_hand.most_common_value:
            return Winner.Player1
        else:
            if first_hand.second_most_common_value < second_hand.second_most_common_value:
                return Winner.Player2
            elif first_hand.second_most_common_value > second_hand.second_most_common_value:
                return Winner.Player1
            else:
                if first_hand.card_values < second_hand.card_values:
                    return Winner.Player2
                elif first_hand.card_values > second_hand.card_values:
                    return Winner.Player1
                else:
                    return Winner.NONE


def main() -> None:
    first_player_hands, second_player_hands = read_file(RESOURCE_DIR / 'problem_54_poker.txt')
    first_player_wins, second_player_wins = 0, 0

    for first_hand, second_hand in zip(first_player_hands, second_player_hands):
        winner = find_winner(first_hand, second_hand)

        if winner == Winner.Player1:
            first_player_wins += 1
        elif winner == Winner.Player2:
            second_player_wins += 1

    print(f'First player: {first_player_wins}')
    print(f'Second player: {second_player_wins}')


if __name__ == "__main__":
    main()
