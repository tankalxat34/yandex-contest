import os
os.chdir(os.getcwd() + "\\cup_backend")

### ### ### ###

import sys

GAMER1 = "Vasya"
GAMER2 = "Petya"
DRAW = "Draw"

winner = DRAW

score = {
    GAMER1: 0,
    GAMER2: 0,
    "uncollected_sum": 0
}

with open("input.txt", "r", encoding="UTF-8") as file:
    K, N = list(map(int, file.readline().split()))
    CARDS = list(map(int, file.readline().split()))


def writeAnswer(answer: str):
    open("output.txt", "w", encoding="UTF-8").write(answer)
    sys.exit(0)

for card_int in CARDS:
    if card_int % 5 == 0:
        score[GAMER1] += 1
    elif card_int % 3 == 0:
        score[GAMER2] += 1

    if score[GAMER1] >= K:
        winner = GAMER1
        writeAnswer(winner)
    elif score[GAMER2] >= K:
        winner = GAMER2
        writeAnswer(winner)


if score[GAMER2] < K and score[GAMER1] < K:
    if score[GAMER1] > score[GAMER2]:
        winner = GAMER1
        writeAnswer(winner)
    elif score[GAMER2] > score[GAMER1]:
        winner = GAMER2
        writeAnswer(winner)
    else:
        winner = DRAW
        writeAnswer(winner)
        

with open("output.txt", "w", encoding="UTF-8") as file:
    file.write(winner)
