from collections import deque
T = 10
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    dic = {}
    for i in range(N//2):
        if dic.get(lst[i*2]) == None:
            dic[lst[i * 2]] = [lst[i*2+1]]
        else:
            dic[lst[i*2]].append(lst[i*2+1])
    q = deque([(M, 0)])
    visited = [False] * 101
 
    result = []
    while q:
        key, count = q.popleft()
        if not visited[key]:
            result.append((key, count))
        visited[key] = True
        if dic.get(key) != None:
            for i in dic[key]:
                if not visited[i]:
                    q.append((i, count+1))
    result.sort(key=lambda x:(x[1], x[0]))
    print(f'#{tc} {result[-1][0]}')