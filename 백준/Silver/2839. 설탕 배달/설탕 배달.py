import sys
N = int(sys.stdin.readline())
limit = N // 5
flag = False

for i in range(limit, -1, -1):
    val = N - (i * 5)
    if val % 3 == 0:
        print(i + val // 3)
        flag = True
        break
if not flag:
    print(-1)