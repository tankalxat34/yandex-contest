import os
os.chdir("task_a")


def setIntWithProverka(e):
    if 1 <= int(e) and int(e) <= 10**9:
        return int(e)
    else:
        print(-1)
        open("output.txt", "w").write(str(-1))
        quit()

try:
    N = int(input())
    V = list(map(lambda e: setIntWithProverka(e), input().split(" ")))
except ValueError:
    f = open("input.txt")
    content = f.readlines()
    N = int(content[0])
    V = list(map(lambda e: setIntWithProverka(e), content[1].split(" ")))
    f.close()

if not (len(V) == N or not (1 <= N and N <= 100000)):
    print(-1)
    open("output.txt", "w").write(str(-1))
    quit()

mx_v = max(V)
k = 0
counter = 0
while len(set(V)) != 1:
    for i in range(len(V)):
        if V[i] != mx_v:
            k += 1

    for k_value in range(k):
        V[k_value] += 1
    counter += 1

    k = 0

    if counter >= 1000:
        print(-1)
        open("output.txt", "w").write(str(-1))
        quit()


print(counter)
open("output.txt", "w").write(str(counter))
