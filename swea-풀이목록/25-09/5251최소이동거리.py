import heapq
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    dic = {i:[] for i in range(N+1)}
    distances = {i:float('inf') for i in range(N+1)}
    distances[0] = 0
    for i in range(E):
        a,b,w = map(int, input().split())
        dic[a].append((w, b))
    pq = []
    heapq.heappush(pq, (0, 0))
    while pq:
        distance, node = heapq.heappop(pq)
        if distance > distances[node]:
            continue
        for w, next_node in dic[node]:
            if distance + w < distances[next_node]:
                distances[next_node] = distance+w
                heapq.heappush(pq, (distance + w, next_node))
    print(f'#{tc} {distances[N]}')