import os
os.chdir(os.getcwd() + "\\cup_backend")

### ### ### ###

"""
Даны две строки строчных латинских символов: строка J и строка S. Символы, входящие в строку J, — «драгоценности», входящие в строку S — «камни». Нужно определить, какое количество символов из S одновременно являются «драгоценностями». Проще говоря, нужно проверить, какое количество символов из S входит в J.
"""


def mystrip(string: str):
    return string.strip()


with open("input.txt", "r", encoding="UTF-8") as file:
    j, s = list(map(mystrip, file.readlines()))

counter = 0

for symbol in s:
    if symbol in j:
        counter += 1

with open("output.txt", "w", encoding="UTF-8") as file:
    file.write(str(counter))
