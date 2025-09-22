from collections import deque
T = 10
for tc in range(1, T+1):
    testcase = int(input())
    lst = [list(map(int, input().strip())) for _ in range(16)]
    wasd = [(0,1), (1,0), (-1,0), (0,-1)]
    q = deque()
    for i in range(16):
        for j in range(16):
            if lst[i][j] == 2:
                 q.append((i, j))
                 break
 
    is_valid = False
    while q:
        x,y = q.popleft()
        lst[x][y] = 1
        for dx, dy in wasd:
            nx, ny = dx+x, dy+y
            if 0 <= nx < 16 and 0 <= ny < 16:
                if not lst[nx][ny]:
                    q.append((nx,ny))
                if lst[nx][ny] == 3:
                    is_valid = True
                    break
    if is_valid:
        print(f'#{testcase} 1')
    else:
        print(f'#{testcase} 0')