import pytest

from main import Hand, Card


@pytest.mark.parametrize("cards, expected", [
    (["2d", "3d", "4d", "5d", "6d"], 6),
    (["7d", "8d", "9d", "Td", "Jd"], 6),
    (["2d", "3d", "4d", "5d", "6s"], 0),
])
def test_flush(cards, expected):
    result = Hand(cards).flush()
    assert result == expected


@pytest.mark.parametrize("card, expected", [
    ("2d", 2),
    ("3d", 3),
    ("4d", 4),
    ("5d", 5),
    ("6d", 6),
    ("7d", 7),
    ("8d", 8),
    ("9d", 9),
    ("Td", 10),
    ("Jd", 11),
    ("Qd", 12),
    ("Kd", 13),
    ("Ad", 14),
])
def test_cards(card, expected):
    result_card = Card(card)
    assert result_card.suit == card[1]
    assert result_card.rank == expected


@pytest.mark.parametrize("cards, expected", [
    (["2d", "3d", "4d", "5d", "6d"], 5),
    (["7d", "8d", "9d", "Td", "Jd"], 5),
    (["2d", "3d", "4d", "5d", "Qs"], 0),
])
def test_straight(cards, expected):
    result = Hand(cards).straight()
    assert result == expected


@pytest.mark.parametrize("cards, expected", [
    (["Td", "Jd", "Qd", "Kd", "Ad"], 10),  # RF
    (["7d", "8d", "9d", "Td", "Jd"], 9),  # SF
    (["9d", "9c", "9h", "9s", "2s"], 8),  # Four of a kind
    (["9d", "9c", "9h", "2s", "2s"], 7),  # Full house
    (["2d", "3d", "4d", "5d", "6s"], 5),  # Straight
    (["9d", "9c", "9h", "2s", "3s"], 4),  # Three of a kind
    (["9d", "9c", "2h", "2s", "3s"], 3),  # Two pair
    (["9d", "9c", "2h", "5s", "3s"], 2),  # One pair
    (["2d", "Jd", "4d", "5d", "Qs"], 1),  # High card

])
def test_make_math(cards, expected):
    result = Hand(cards).make_math()
    assert result == expected


@pytest.mark.parametrize("cards, expected", [
    (["9d", "9c", "9h", "9s", "2s"], 8),  # Four of a kind
    (["9d", "9c", "9h", "2s", "2s"], 7),  # Full house
    (["9d", "9c", "2h", "2s", "3s"], 3),  # Two pair
    (["9d", "9c", "2h", "5s", "3s"], 2),  # One pair
    (["2d", "Jd", "4d", "5d", "Qs"], 0),
])
def test_pair(cards, expected):
    result = Hand(cards).pair()
    assert result == expected
