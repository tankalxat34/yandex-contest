def resolveTask(inputFile="input.txt", outputFile="output.txt"):

    with open(inputFile, "r", encoding="utf-8") as file:
        CONTENT = file.readlines()

    T = int(CONTENT[0])
    ROOMS = tuple(map(lambda e: e.strip(), CONTENT[1:]))

    counter = 1

    G = {}

    for room in ROOMS:
        for i in range(len(room) - 2):
            counter += 1

            start = room[i:i+3]
            end = room[i+1:i+4]

            if (len(start) and len(end)) == 3:
                try:
                    G[start][end] += 1
                except Exception:
                    try:
                        G[start][end] = 1
                    except Exception:
                        G[start] = {}
                        G[start][end] = 1

    answer = ""
    resultString = ""

    e = 0

    for start in G.keys():
        for end in G[start].keys():
            e += 1
            resultString += f"{start} {end} {G[start][end]}\n"

    answer += f"{len(G.keys())}\n{e}\n{resultString}"

    with open(outputFile, "w", encoding="UTF-8") as file:
        file.write(answer[:-1])

for i in range(1, 5):
    resolveTask(f"input{i}.txt", f"output{i}.txt")
