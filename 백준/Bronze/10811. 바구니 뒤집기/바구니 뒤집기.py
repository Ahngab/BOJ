N, M = map(int, input().split())
arr  = [i for i in range(1, N+1)]

for i in range(M):
    i, j = map(int, input().split())
    arr[i-1:j] = reversed(arr[i-1:j])

print(*arr)