import sys
from collections import deque

M , N = map(int, sys.stdin.readline().strip().split())
arr = deque(map(int, sys.stdin.readline().strip().split()))
temp = [0] * (M+1)

for i in range(M):
    temp[i+1] = temp[i] + arr[i]

for _ in range(N):
    n, m = map(int, sys.stdin.readline().strip().split())
    print(temp[m] - temp[n-1])