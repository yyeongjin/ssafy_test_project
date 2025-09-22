T = 10
for tc in range(1, T+1):
    N,M = map(int, input().split())
    lst = list(map(int, input().split()))
    visited = [False] * 100
    result_cnt = 0
    dic = {}
 
    for i in range(0, len(lst), 2):
        idx = i+1
        if dic.get(lst[i]) == None:
            dic[lst[i]] = [lst[idx]]
        else:
            dic[lst[i]].extend([lst[idx]])
 
    def dfs(cnt, dic):
        global visited, result_cnt
        if cnt == 99:
            result_cnt = 1
            return
        if dic.get(cnt) == None:
            return
        for i in dic[cnt]:
            if not visited[i]:
                visited[i] = True
                dfs(i, dic)
    dfs(N, dic)
    print(f'#{tc} {result_cnt}')