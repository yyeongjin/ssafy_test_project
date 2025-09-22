T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    max_set = set()
    def dfs(score, kcal, idx):
        global max_set
        if kcal > L:
            return
        if kcal <= L:
            if score not in max_set:
                max_set.add(score)
        if idx == N:
            return
        dfs(score+lst[idx][0], kcal+lst[idx][1], idx+1)
        dfs(score, kcal, idx+1)
    dfs(0,0,0)
    print(f'#{tc} {max(max_set)}')