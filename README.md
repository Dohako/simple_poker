# Poker

Of course, it can be improved, but for now, let's just focus on getting the score of a hand of poker.

## Input

- A string of 5 cards, separated by spaces. Each card is represented by two characters. The first character is the value (one of `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `T`, `J`, `Q`, `K`, `A`), and the second character is the suit (one of `h`, `d`, `c`, `s`).
- Example: `2h 3h 4h 5h 6h`

## Output

A score of the hand, according to the following rules:

- A high card is worth 1 point.
- A pair is worth 2 points.
- Two pairs are worth 3 points.
- Three of a kind is worth 4 points.
- A straight is worth 5 points.
- A flush is worth 6 points.
- A full house is worth 7 points.
- Four of a kind is worth 8 points.
- A straight flush is worth 9 points.
- A royal flush is worth 10 points.

## Examples

- `2h 3h 4h 5h 6h` -> 5
- `2h 2d 4h 4h 6h` -> 3
- `2h 2d 2h 4h 6h` -> 4
- `2h 3h 4h 5h 7h` -> 6
- `2h 2d 4h 4h 4h` -> 7
- `2h 2d 2h 2h 6h` -> 8
- `2h 3h 4h 5h 6h` -> 9
- `Th Jh Qh Kh Ah` -> 10
