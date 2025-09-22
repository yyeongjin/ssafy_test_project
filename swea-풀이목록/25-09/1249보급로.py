from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())  
    lst = [list(map(int, input().strip())) for _ in range(N)]  
    distance = [[-1] * N for _ in range(N)]  
    q = deque([(0, 0)]) 
    distance[0][0] = lst[0][0] 
 
    wasd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
 
    while q:
        x, y = q.popleft()
 
        for dx, dy in wasd:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N: 
                new_dist = distance[x][y] + lst[nx][ny] 
                if distance[nx][ny] == -1 or new_dist < distance[nx][ny]:
                    distance[nx][ny] = new_dist
                    q.append((nx, ny))
 
    print(f'#{tc} {distance[N-1][N-1]}')