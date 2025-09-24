import heapq
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())
 
    lst = []
    for i in range(N):
        lst.append((x_lst[i], y_lst[i]))
 
    visited = set()
    pq = []
    total_cost = 0.0
    total_island = 0
    heapq.heappush(pq, (0,0))
 
    while pq and total_island < N:
        cost, island = heapq.heappop(pq)
        if island in visited:
            continue
        visited.add(island)
        total_cost += cost
        total_island += 1
        for new_island in range(N):
            if new_island not in visited:
                dist = (lst[new_island][0] - lst[island][0]) ** 2 + \
                          (lst[new_island][1] - lst[island][1]) ** 2
                new_cost = E * dist
                heapq.heappush(pq, (new_cost, new_island))
    print(f'#{tc} {round(total_cost)}')