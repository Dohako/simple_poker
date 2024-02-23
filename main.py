
CARD_RANK_MAPPING = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


class Card:
    def __init__(self, value: str):
        self.rank = CARD_RANK_MAPPING[value[0]]
        self.suit = value[1]


class Hand:
    def __init__(self, cards: list[str]):
        self.cards = [Card(card) for card in cards]
        self.sorted_card = sorted(self.cards, key=lambda x: x.rank)

    def make_math(self):
        flush = self.flush()
        straight = self.straight()
        if flush and straight and self.sorted_card[0].rank == 10:
            return 10
        elif flush and straight:
            return 9
        pair = self.pair()
        return max(flush, straight, pair, 1)

    def flush(self):
        if len({card.suit for card in self.cards}) > 1:
            return 0
        return 6

    def straight(self):
        if self.sorted_card[-1].rank - self.sorted_card[0].rank == 4:
            return 5
        return 0

    def pair(self):
        result = {}
        for card in self.cards:
            if card.rank in result:
                result[card.rank] += 1
            else:
                result[card.rank] = 1
        values = list(result.values())
        result = 0
        if 2 in values and 3 in values:
            result = 7
        elif 4 in values:
            result = 8
        elif 3 in values:
            result = 4
        elif values.count(2) == 2:
            result = 3
        elif 2 in values:
            result = 2
        return result

    def royal_flush(self):
        if self.sorted_card[0].rank == 10 and self.flush():
            return 10
        return 0
