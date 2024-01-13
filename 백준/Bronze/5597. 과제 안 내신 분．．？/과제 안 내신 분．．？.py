temp = [0]*30

for _ in range(28):
    temp[int(input()) - 1] = 1

for i in range(30):
    if temp[i] == 0:
        print(i + 1)