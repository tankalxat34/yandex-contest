# input_file = "input.txt"
input_file = "cup_training_algorithms/input.txt"

with open(input_file, "r", encoding="utf-8") as file:
    h, m = list(map(int, file.read().split()))

# print(h, m)

new_h = 0
new_m = 0

# work with hours
# if h <= 6:
new_h = 12 - h
new_m = 60 - m

if new_m == 60:
    new_m = 0
if new_h == 12:
    new_h = 0

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(f"{new_h} {new_m}")
# print(new_h, new_m)