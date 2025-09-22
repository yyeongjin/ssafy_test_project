from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(str, input().strip())) for _  in range(N)]
    wasd = [(0,1),(1,0),(0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lst[i][j] == "*":
                visited[i][j] = True
    def wasd_func(x,y):
        for dx, dy in wasd:
            if 0 <= dx+x < N and 0 <= dy+y < N:
                if lst[dx+x][dy+y] == '*':
                    return False
        return True
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and wasd_func(i, j):
                count += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    x,y = q.popleft()
                    if wasd_func(x,y):
                        for dx, dy in wasd:
                            if 0 <= dx+x < N and 0 <= dy+y < N:
                                if not visited[dx+x][dy+y]:
                                    visited[dx+x][dy+y] = True
                                    q.append((dx+x,dy+y))
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                count += 1
    print(f'#{tc} {count}')
