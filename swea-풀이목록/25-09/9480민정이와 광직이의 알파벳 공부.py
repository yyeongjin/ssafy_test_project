T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(str, input().strip())) for _ in range(N)]
    result = set()
    count = 0
    def dfs(result_lst, idx):
        global count, result
        result_set = set(result_lst)
        if len(result_set) == 26:
            result.add(''.join(result_lst))
        if idx == N:
            return
        dfs(result_lst + lst[idx], idx+1)
        dfs(result_lst, idx+1)
    dfs([], 0)
    print(f'#{tc} {len(result)}')