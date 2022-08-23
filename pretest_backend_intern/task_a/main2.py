import os
os.chdir("task_a")


def setIntWithProverka(e, userInput):
    if 1 <= int(e) and int(e) <= 10**9:
        return int(e)
    else:
        if userInput:
            print(-1)
        else:
            open("output.txt", "w").write(str(-1))
        quit()

userInput = True
try:
    N = int(input())
    V = list(map(lambda e, userInput=userInput: setIntWithProverka(e, userInput), input().split(" ")))
except ValueError:
    userInput = False
    f = open("input.txt")
    content = f.readlines()
    N = int(content[0])
    V = list(map(lambda e, userInput=userInput: setIntWithProverka(e, userInput), content[1].split(" ")))
    f.close()

if not (len(V) == N or not (1 <= N and N <= 100000)):
    if userInput:
        print(-1)
    else:
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
        if userInput:
            print(-1)
        else:
            open("output.txt", "w").write(str(-1))
        quit()


if userInput:
        print(counter)
else:
    open("output.txt", "w").write(str(counter))
