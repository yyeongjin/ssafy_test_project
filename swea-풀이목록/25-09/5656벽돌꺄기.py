from collections import deque
from copy import deepcopy
 
def gravity(board):
    for i in range(W):
        temp_lst = []
        for j in range(H - 1, -1, -1):
            if board[j][i]:
                temp_lst.append(board[j][i])
                board[j][i] = 0
 
        if temp_lst:
            for k in range(len(temp_lst)):
                board[H - k - 1][i] = temp_lst[k]
    return board
 
def bfs(board, x, y):
    q = deque([(x,y)])
    while q:
        board_x,board_y = q.popleft()
        count = board[board_x][board_y]
        board[board_x][board_y] = 0
        if count < 2:
            continue
        for dx, dy in wasd:
            for cnt in range(1, count):
                nx, ny = board_x + dx*cnt, board_y + dy*cnt
                if 0 <= nx < H and 0 <= ny < W:
                    q.append((nx, ny))
    return gravity(board)
 
def dfs(depth, board):
    global result_cnt
    if depth == N:
        result = 0
        for i in range(H):
            for j in range(W):
                if board[i][j] > 0:
                    result += 1
        result_cnt = min(result, result_cnt)
        return
 
    for i in range(W):
        new_lst = deepcopy(board)
        for j in range(H):
            if new_lst[j][i]:
                new_board = bfs(new_lst, j, i)
                dfs(depth + 1, new_board)
                break
    else:
        dfs(depth + 1, new_lst)
 
T = int(input())
for tc in range(1, T+1):
    N,W,H = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(H)]
    wasd = [(1,0), (0,1), (-1,0), (0,-1)]
    result_cnt = float('inf')
    dfs(0, lst)
    print(f'#{tc} {result_cnt}')
