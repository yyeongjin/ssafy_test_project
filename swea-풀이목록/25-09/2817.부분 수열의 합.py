T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    count = 0
    result = set()
    def dfs(idx, total):
        global count
        if total == K:
            count += 1
            return
        if idx == N:
            return
        dfs(idx+1, total)
        dfs(idx+1, total+lst[idx])
    dfs(0, 0)
    print(f'#{tc} {count}')