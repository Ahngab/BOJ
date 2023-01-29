import sys
from collections import deque

def BFS(a, b):
    global field, M, N

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append( (a,b) )
    field[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append( (nx, ny ))

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, K = map(int, sys.stdin.readline().strip().split())
        cnt = 0
        field = [[0 for _ in range(M)] for _ in range(N)]

        for _ in range(K):
            i, j = map(int, sys.stdin.readline().strip().split())
            field[i][j] = 1

        for i in range(N):
            for j in range(M):
                if field[i][j] == 1:
                    BFS(i, j)
                    cnt += 1
        print(cnt)