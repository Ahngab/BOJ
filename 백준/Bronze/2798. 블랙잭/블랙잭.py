N, limit = map(int, input().split())
max_num = 0
data = list(map(int, input().split()))

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if (data[i] + data[j] + data[k]) > limit:
                continue
            else:
                max_num = max(max_num, data[i] + data[j] + data[k])
print(max_num)