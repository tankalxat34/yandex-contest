import os
os.chdir(os.getcwd() + "\\cup_backend")

### ### ### ###

GAMER1 = "Vasya"
GAMER2 = "Petya"

winner = ""

score = {
    GAMER1: 0,
    GAMER2: 0,
    "uncollected_sum": 0
}

with open("input.txt", "r", encoding="UTF-8") as file:
    K, N = list(map(int, file.readline().split()))
    CARDS = list(map(int, file.readline().split()))


for card_int in CARDS:
    if card_int % 5 == 0:
        score[GAMER1] += 1
    elif card_int % 3 == 0:
        score[GAMER2] += 1
    elif not(card_int % 3 == 0 and card_int % 5 == 0) or not(card_int % 3 == 1 and card_int % 5 == 1):
        score["uncollected_sum"] += 1
    
# проверка на победителя
if score[GAMER1] >= K:
    winner = GAMER1
elif score[GAMER2] >= K:
    winner = GAMER2
else:
    if score[GAMER1] > score[GAMER2]:
        winner = GAMER1
    elif score[GAMER1] < score[GAMER2]:
        winner = GAMER2
    else:
        winner = ""

with open("output.txt", "w", encoding="UTF-8") as file:
    file.write(winner)
