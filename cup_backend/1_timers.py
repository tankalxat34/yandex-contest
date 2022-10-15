import os
os.chdir(os.getcwd() + "\\cup_backend")

### ### ### ###

with open("input.txt", "r", encoding="UTF-8") as file:
    N, X, K = list(map(int, file.readline().split()))
    TIMERS = list(map(int, file.readline().split()))

# список для указания времени звонков всех будильников подряд
# нужен для получения времени всех ближайших звонков
all_times_to_call = TIMERS.copy()

# получаем ближайшие звонки
for iteration in range(1, N):
    for timer in TIMERS:
        all_times_to_call.append(timer + X * iteration)
# сортируем от меньшего к большему
all_times_to_call.sort()

# уничтожаем одинаковые звонки будильников
all_times_to_call = list(set(all_times_to_call))

with open("output.txt", "w", encoding="UTF-8") as file:
    file.write(str(all_times_to_call[K - 1]))