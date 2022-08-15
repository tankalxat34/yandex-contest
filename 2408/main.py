def saveOutput(result_dict, output_filename="output.txt"):
    """Сохраняет результат работы программы в файл"""
    # Строковая переменная, в которую запишем результат
    resultFileContent = str()

    # Количество вершин v в графе
    v = len(result_dict.keys())

    # Количество пар вершин e, между которыми есть ориентированные ребра
    e = 0

    for start_point in result_dict.keys():
        for end_point in result_dict[start_point].keys():
            e += 1
            resultFileContent += f"{start_point} {end_point} {result_dict[start_point][end_point]}\n"

    with open(output_filename, "w", encoding="UTF-8") as file:
        file.write(f"{v}\n{e}\n{resultFileContent}")


with open("input.txt", "r", encoding="UTF-8") as file:
    FILECONTENT = file.readlines()

COMBINATIONS = list(map(lambda e: e.strip(), FILECONTENT[1:]))
T = int(FILECONTENT[0])

G = {}

for j in range(T):
    for i in range(len(COMBINATIONS[j]) - 2):
        start_point = COMBINATIONS[j][i:i+3]
        end_point = COMBINATIONS[j][i+1:i+4]

        if len(start_point) == 3 and len(end_point) == 3:
            try:
                G[start_point][end_point] += 1
            except KeyError:
                try:
                    G[start_point][end_point] = 1
                except KeyError:
                    G[start_point] = {}
                    G[start_point][end_point] = 1

saveOutput(G)
