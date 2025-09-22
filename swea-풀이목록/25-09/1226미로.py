t = 10
for tc in range(1, t+1):
    testcase = int(input())
    lst = [list(map(int, input().strip())) for _  in range(16)]
    wasd = [(1,0), (0,1), (-1,0), (0,-1)]
 
    start_wasd = (0,0)
    for i in range(16):
        for j in range(16):
            if lst[i][j] == 2:
                start_wasd = (i,j)
                break
 
    is_valid = False
    def dfs(x, y):
        global is_valid
        if lst[x][y] == 3:
            is_valid = True
        if lst[x][y] == 1:
            return
        if lst[x][y] == 0:
            lst[x][y] = 1
        for dx, dy in wasd:
            if 0 < x+dx < 16 and 0 < y+dy < 16:
                dfs(dx+x, dy+y)
 
    x,y = start_wasd
    dfs(x,y)
    if is_valid == True:
        print(f'#{testcase} 1')
    else:
        print(f'#{testcase} 0')