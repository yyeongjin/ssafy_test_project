T = int(input())
for tc in range(1, T+1):
    V, E  = map(int, input().split())
    dic = {}
    for i in range(1, E+1):
        S, G = map(int, input().split())
        if dic.get(S) == None:
            dic[S] = [G]
        else:
            dic[S].append(G)
    S, G = map(int, input().split())
    is_valid = False
    visited = set()
    def dfs(node, visited):
        global is_valid
        if node == G:
            is_valid = True
            return
        if dic.get(node) == None:
            return
        visited.add(node)
        for i in dic[node]:
            if i not in visited:
                dfs(i, visited)
    dfs(S, visited)
    if is_valid:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')