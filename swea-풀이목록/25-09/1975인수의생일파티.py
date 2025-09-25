import heapq
T = int(input())
for tc in range(1, T+1):
    N,M,X = map(int, input().split())
    dic = {i:[] for i in range(1, N+1)}
    dic1 = {i:[] for i in range(1, N+1)}
    for i in range(M):
        x,y,c = map(int, input().split())
        dic[x].append((c,y))
        dic1[y].append((c,x))
 
    distances = [float('inf') for i in range(N+1)]
    distances[X] = 0
    distances1 = [float('inf') for i in range(N+1)]
    distances1[X] = 0
 
 
    pq = []
    heapq.heappush(pq, (0,X))
    while pq:
        w, node = heapq.heappop(pq)
        if w > distances[node]:
            continue
        for ww, next_node in dic[node]:
            new_dist = ww + w
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    pq = []
    heapq.heappush(pq, (0,X))
    while pq:
        w, node = heapq.heappop(pq)
        if w > distances1[node]:
            continue
        for ww, next_node in dic1[node]:
            new_dist = ww + w
            if new_dist < distances1[next_node]:
                distances1[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
 
    for i in range(len(distances)):
        distances[i] = distances[i] + distances1[i]
        if distances[i] == float("inf"):
            distances[i] = 0
 
    print(f'#{tc} {max(distances)}')