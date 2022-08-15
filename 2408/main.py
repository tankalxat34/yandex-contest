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

# Программа работает только если она запускается на прямую, не импортируется
if __name__ == "__main__":
    # Читаем файл построчно
    with open("input.txt", "r", encoding="UTF-8") as file:
        FILECONTENT = file.readlines()
    
    # Создаем список строк. У каждой строки слева и справа обрезаем пробелы
    COMBINATIONS = list(map(lambda e: e.strip(), FILECONTENT[1:]))
    # Сохраняем количество переговорок
    T = int(FILECONTENT[0])

    # Словарь для будущего графа
    G = {}

    # Цикл для каждой строки
    for j in range(T):
        # Цикл для каждого символа в строке
        for i in range(len(COMBINATIONS[j]) - 2):
            # Создаем начальную и конечную вершины графа
            start_point = COMBINATIONS[j][i:i+3]
            end_point = COMBINATIONS[j][i+1:i+4]

            # Если количество символов в вершинах равно 3
            if len(start_point) == 3 and len(end_point) == 3:
                # Пытаемся инкрементировать счетчик для конкретных вершин
                try:
                    G[start_point][end_point] += 1
                except KeyError:
                    # Если счетчика для конкретных вершин не существует
                    try:
                        # Пытаемся инициализировать его
                        G[start_point][end_point] = 1
                    except KeyError:
                        # Если же в start_point нет такой конечной вершиныы, создаем ее и инициализируем в ней счетчик
                        G[start_point] = {}
                        G[start_point][end_point] = 1

    saveOutput(G)
