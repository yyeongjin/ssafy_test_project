T = int(input())
for tc in range(1, T + 1):
    lst = [list(map(str, input().split())) for _ in range(4)]
    wasd = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = set()
 
 
    def dfs(total, depth, x, y):
        global result
        if depth == 7:
            if total not in result:
                result.add(total)
            return
        for dx, dy in wasd:
            if 0 <= dx + x < 4 and 0 <= dy + y < 4:
                dfs(total + lst[dx + x][dy + y], depth + 1, dx + x, dy + y)
 
 
    for i in range(4):
        for j in range(4):
            dfs(lst[i][j], 1, i, j)
 
    print(f'#{tc} {len(result)}')