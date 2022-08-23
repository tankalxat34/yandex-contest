import os
os.chdir("task_a")



class Vessels:
    def __init__(self, line, inputByUser = False):
        self.vessels = list(map(int, line.split()))
        self.operation_counter = 0
        self.inputByUser = inputByUser

    def spillAcid(self, k):
        if self.operation_counter >= 1000:
            self.saveResult(-1)
            quit()
        else:
            for i in range(k):
                self.vessels[i] += 1
            self.operation_counter += 1

    def get(self):
        return self.vessels
    
    def saveResult(self, result):
        if self.inputByUser:
            print(result)
        else:
            with open("output.txt", "w", encoding="UTF-8") as file:
                file.write(str(result))

    def checkToCorrectData(self):
        if 1 <= n and n <= 100000:
            for e in self.vessels:
                if not(1 <= e and e <= 10**9):
                    self.saveResult(-1)
                    quit()
            return True
        else:
            self.saveResult(-1)


fromInput = True
N = input()
VESSELS = input()
if not (N and VESSELS):
    fromInput = False

    f = open("input.txt", "r", encoding="utf-8")
    CONTENT = f.readlines()
    f.close()

    n = int(CONTENT[0])
    vessels = Vessels(CONTENT[1])
else:
    n = int(N)
    vessels = Vessels(VESSELS, True)

vessels.checkToCorrectData()

if n != len(vessels.get()):
    vessels.saveResult(-1)
    quit()

max_vessel = max(vessels.get())

counter = 0
while len(set(vessels.vessels)) != 1:
    for vessel in vessels.get():
        if vessel != max_vessel:
            counter += 1
    vessels.spillAcid(counter)
    counter = 0

vessels.saveResult(vessels.operation_counter)