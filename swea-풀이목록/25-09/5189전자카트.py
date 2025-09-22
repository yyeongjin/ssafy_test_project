T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
 
    visited = [False] * N
    result = float('inf')
 
    def dfs(idx, total, count):
        global result
        if count == N:
            result = min(result, total + lst[idx][0])
            return
        for i in range(N):
            if not visited[i] and lst[idx][i] != 0:
                visited[i] = True
                dfs(i, total + lst[idx][i], count + 1)
                visited[i] = False
    visited[0] = True
    dfs(0, 0, 1)
 
    print(f'#{tc} {result}')