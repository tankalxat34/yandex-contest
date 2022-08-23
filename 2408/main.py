def saveOutput(result_dict, output_filename="output.txt", userInput=False):
    """Сохраняет результат работы программы в файл"""
    # Строковая переменная, в которую запишем результат
    resultFileContent = str()

    # Количество вершин v в графе
    v = len(result_dict.keys())

    # Количество пар вершин e, между которыми есть ориентированные ребра
    e = 0

    # Для каждой стартовой вершины
    for start_point in result_dict.keys():
        # Для каждой конечной вершины
        for end_point in result_dict[start_point].keys():
            # Инкрементируем общее количество конечных вершин
            e += 1
            # В результат добавляем строку в нужном формате
            resultFileContent += f"{start_point} {end_point} {result_dict[start_point][end_point]}\n"

    # Записываем результат в необходимом формате в файл
    if userInput:
        print(f"{v}\n{e}\n{resultFileContent}"[:-1])
    else:
        with open(output_filename, "w", encoding="UTF-8") as file:
            file.write(f"{v}\n{e}\n{resultFileContent}"[:-1])


# Программа работает только если она запускается на прямую, не импортируется
if __name__ == "__main__":
    userInput = True
    # Читаем файл построчно
    T = input()
    if not T:
        userInput = False
        with open("input.txt", "r", encoding="UTF-8") as file:
            FILECONTENT = file.readlines()

        # Создаем список строк. У каждой строки слева и справа обрезаем пробелы
        COMBINATIONS = list(map(lambda e: e.strip(), FILECONTENT[1:]))
        # Сохраняем количество переговорок
        T = int(FILECONTENT[0])
    else:
        T = int(T)
        COMBINATIONS = []
        for i in range(T):
            COMBINATIONS.append(input().strip())


    # Словарь для будущего графа
    G = {}

    # Цикл для каждой строки
    if T >= 1 and T <= 40000:
        for j in range(T):
            # Цикл для каждого символа в строке
            for i in range(len(COMBINATIONS[j]) - 2):
                # Создаем начальную и конечную вершины графа
                if len(COMBINATIONS[j]) >= 4 and len(COMBINATIONS[j]) <= 30:
                    start_point = COMBINATIONS[j][i:i+3]
                    end_point = COMBINATIONS[j][i+1:i+4]

                    # Если количество символов в вершинах равно 3
                    if len(start_point) == 3 and len(end_point) == 3 and start_point == start_point.lower() and end_point == end_point.lower():
                        # Пытаемся инкрементировать счетчик для конкретных вершин
                        try:
                            G[start_point][end_point] += 1
                        except KeyError:
                            # Если счетчика для конкретных вершин не существует
                            try:
                                # Пытаемся инициализировать его
                                G[start_point][end_point] = 1
                            except KeyError:
                                # Если же в start_point нет такой конечной вершины, создаем ее и инициализируем в ней счетчик
                                G[start_point] = {}
                                G[start_point][end_point] = 1

    saveOutput(G, "output.txt", userInput)
