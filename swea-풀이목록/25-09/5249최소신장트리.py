import heapq
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    dic = {i: [] for i in range(V+1)}
 
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        dic[n1].append((n2, w))
        dic[n2].append((n1, w))
 
    visited = [False] * (V+1)
    pq = []
    total_weight = 0
 
    heapq.heappush(pq, (0, 0))
 
    while pq:
        w, node = heapq.heappop(pq)
 
        if visited[node]:
            continue
 
        visited[node] = True
        total_weight += w
 
        for next_node, weight in dic[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (weight, next_node))
 
    print(f'#{tc} {total_weight}')