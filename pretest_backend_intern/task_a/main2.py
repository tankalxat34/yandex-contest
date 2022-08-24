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

cnt = 0
for i in range(1, len(V)):
    d = V[i] - V[i-1]
    if d < 0:
        cnt = -1
    elif d > 0:
        cnt += d

print(cnt)
open("output.txt", "w").write(str(cnt))
