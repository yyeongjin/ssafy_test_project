T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, str(N)))
    N_len = len(lst)
    max_result = float("-inf")
    visited = set()
 
    def dfs(cnt, lst):
        global max_result
        result = int("".join(map(str, lst)))
        if (cnt, result) in visited:
            return
        visited.add((cnt, result))
        if cnt == M:
            if max_result < result:
                max_result = result
            return
        for i in range(N_len):
            for j in range(i+1, N_len):
                lst[i], lst[j] = lst[j], lst[i]
                dfs(cnt+1, lst)
                lst[i], lst[j] = lst[j], lst[i]
    dfs(0, lst)
    print(f'#{tc} {max_result}')