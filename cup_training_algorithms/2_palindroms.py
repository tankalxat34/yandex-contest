
with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read().strip()

answers = []

for i in range(len(content)):
    for j in range(len(content), 0, -1):
        if content[i:j] == content[i:j][::-1] and len(content[i:j]) >= 2:
            # print(content[i:j])
            answers.append(content[i:j])

answers = list(set(answers))
answers.sort()

# print(answers)



with open("output.txt", "w", encoding="utf-8") as file:
    if not len(answers):
        # print(-1)
        file.write("-1")
    else:
        print(answers)
        file.write(str(answers[0]))
