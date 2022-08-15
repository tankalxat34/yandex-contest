# class Tree:
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right

# t = Tree("a", Tree("c", "b"))
# print(t.right.right)

# a, b, c, d, e, f, g, h = range(8)
# N = [
#     {b: 2, c: 1, d: 3, e: 9, f: 4},  # a
#     {c: 4, e: 3},  # b
#     {d: 8},  # c
#     {e: 7},  # d
#     {f: 5},  # e
#     {c: 2, g: 2, h: 2},  # f
#     {f: 1, h: 6},  # g
#     {f: 9, g: 8}  # h
# ]

# print(N[a][b])

"""
G = [

    {"aaa": ["aaa", 10]},
    {"aaa": ["aab", 2]},
    {"aab": ["abb", 2]},
    {"abb": ["bbb", 2]},
    {"bbb": ["bba", 2]},
    {"bba": ["baa", 2]},
    {"baa": ["aaa", 1]},

    ["aaa", "aaa", 10],
    ["aaa", "aab", 2],
    ["aab", "abb", 2],
    ["abb", "bbb", 2],
    ["bbb", "bba", 2],
    ["bba", "baa", 2],
    ["baa", "aaa", 1],

    {"aaa": {"aaa": 10}},
    {"aaa": {"aab": 2}},
    {"aab": {"abb": 2}},
    {"abb": {"bbb": 2}},
    {"bbb": {"bba": 2}},
    {"bba": {"baa": 2}},
    {"baa": {"aaa": 1}},
]



G = {
    "aaa": {
        "aaa": 10,
        "aab": 2
    },
    "aab": {
        "abb": 2
    }
}

"""

from tracemalloc import start


def printResult(G):
    print(":::ANSWER IS:::")
    print(G)
    print(len(G.keys()))
    for start_point in G.keys():
        for end_point in G[start_point].keys():
            print(start_point, end_point, G[start_point][end_point])
    print(":::END ANSWER:::")


# if __name__ == "__main__":
with open("input.txt", "r", encoding="UTF-8") as file:
    FILECONTENT = file.readlines()
    COMBINATIONS = list(map(lambda e: e.strip(), FILECONTENT[1:]))
    T = int(FILECONTENT[0])

G = {}

counter = 1
start_point = str()

for j in range(T):
    for i in range(len(COMBINATIONS[j]) - 2):

        start_point = COMBINATIONS[j][i:i+3]
        if len(start_point) != 3:
            start_point = COMBINATIONS[j][0:3]

        end_point = COMBINATIONS[j][i+1:i+4]
        if len(end_point) != 3:
            end_point = COMBINATIONS[j][1:4]

        print(counter, start_point, end_point)
        counter += 1

        try:
            G[start_point][end_point] += 1
        except KeyError:
            G[start_point] = {} 
            G[start_point][end_point] = 1
            



    print("=" * 50)
    counter = 1
    print(G)

printResult(G)