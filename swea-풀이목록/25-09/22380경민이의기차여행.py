import heapq
testcase = int(input())
for tc in range(1, testcase+1):
    N, T = map(int, input().split())
    dic = {i:[] for i in range(N)}
    distances = {i:float('inf') for i in range(N)}
    distances[0] = 0
    for i in range(T):
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
 
    if type(distances[N-1]) == float:
        print(f"#{tc} impossible")
    else:
        print(f'#{tc} {distances[N-1]}')