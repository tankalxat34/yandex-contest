# class Tree:
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right

# t = Tree("a", Tree("c", "b"))
# print(t.right.right)

a, b, c, d, e, f, g, h = range(8)
N = [
    {b: 2, c: 1, d: 3, e: 9, f: 4},  # a
    {c: 4, e: 3},  # b
    {d: 8},  # c
    {e: 7},  # d
    {f: 5},  # e
    {c: 2, g: 2, h: 2},  # f
    {f: 1, h: 6},  # g
    {f: 9, g: 8}  # h
]

print(N[a][b])
