import heapq
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    distances =[[float('inf') for _ in range(N)] for _ in range(N)]
    distances[0][0] = 0
    wasd = [(0,1), (1,0), (0,-1), (-1,0)]
    pq = []
    heapq.heappush(pq, (0, 0,0))
 
    while pq:
        distance, x,y = heapq.heappop(pq)
        if distance > distances[x][y]:
            continue
        for dx, dy in wasd:
            nx, ny = dx+x, dy+y
            if 0 <= nx < N and 0 <= ny < N:
                if lst[nx][ny] <= lst[x][y]:
                    cost = 1
                else:
                    cost = (lst[nx][ny] - lst[x][y]) + 1
                new_dist = distance + cost
                if new_dist < distances[nx][ny]:
                    distances[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))
    print(f'#{tc} {distances[N-1][N-1]}')
