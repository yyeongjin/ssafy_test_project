T = int(input())
for tc in range(1, T+1):
        N, M = map(int, input().split())
        dic = {}
        for i in range(M):
            korean1, korean2 = map(int, input().split())
            if dic.get(korean1) == None:
                dic[korean1] = [korean2]
            else:
                dic[korean1].append(korean2)
            if dic.get(korean2) == None:
                dic[korean2] = [korean1]
            else:
                dic[korean2].append(korean1)
        for i in range(1, N+1):
            if dic.get(i) == None:
                dic[i] = []
        visited = [False] * (N+1)
        def dfs(key, dic):
            if dic.get(key) == None:
                return
            visited[key] = True
            for i in dic[key]:
                if not visited[i]:
                    dfs(i, dic)
        count = 0
        for i in dic.keys():
            if not visited[i]:
                count += 1
                dfs(i, dic)
        print(f'#{tc} {count}')