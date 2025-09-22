for tc in range(1, T + 1):
    from copy import deepcopy
 
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    max_cnt = 0
    for i in lst:
        max_cnt = max(max(i), max_cnt)
    wasd = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    wasd_lst = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] == max_cnt:
                wasd_lst.append((i, j))
 
    result = float('-inf')
 
 
    def dfs(x, y, k, cnt, map_lst):
        global result, lst, visited
        result = max(result, cnt)
        for dx, dy in wasd:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                if map_lst[x][y] > map_lst[nx][ny]:
                    dfs(nx, ny, k, cnt + 1, map_lst)
                elif not k:
                    if (map_lst[x][y]) > map_lst[nx][ny] - K:
                        map_lst[nx][ny] = map_lst[x][y] - 1
                        dfs(nx, ny, True, cnt + 1, map_lst)
                        map_lst[nx][ny] = lst[nx][ny]
                visited[nx][ny] = False
 
    for x, y in wasd_lst:
        copy_lst = deepcopy(lst)
        visited[x][y] = True
        dfs(x, y, False, 1, copy_lst)
        visited[x][y] = False
 
    print(f'#{tc} {result}')