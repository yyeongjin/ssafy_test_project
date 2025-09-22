T = int(input())
for tc in range(1, T+1):
    N,L = map(int, input().split())
    lst = [tuple(map(int, input().split())) for _ in range(N)]
    result = float("-inf")
    def dfs(total , k, cnt):
        global result
        if k > L:
            return
        if k <= L:
            result = max(total, result)
        if cnt == N:
            return
        taste, kcal = lst[cnt]
        dfs(total + taste, k + kcal, cnt + 1)
        dfs(total, k, cnt + 1)
    dfs(0,0,0)
    print(f'#{tc} {result}')