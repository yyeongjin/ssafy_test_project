T = int(input())
for tc in range(1, T+1):
    N,M,K = map(int, input().split())
    lst = [[(0,0) for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        y, x, bug, wasd = map(int, input().split())
        lst[y][x] = (bug,wasd)
    result = 0
    def func(cnt, lst):
        global result
        if cnt == M:
            for i in range(N):
                for j in range(N):
                    bug, wasd = lst[i][j]
                    result += bug
            return
        bug_lst = []
        for j in range(N):
            for k in range(N):
                bug, wasd = lst[j][k]
                if bug:
                    lst[j][k] = (0,0)
                    if wasd == 1:
                        if j-1 == 0:
                            bug_lst.append((j-1, k, bug//2, 2))
                            continue
                        else:
                            bug_lst.append((j-1, k, bug, wasd))
 
                    elif wasd == 2:
                        if j+1 == N-1:
                            bug_lst.append((j+1, k, bug//2, 1))
                            continue
                        else:
                            bug_lst.append((j+1, k, bug, wasd))
 
                    elif wasd == 3:
                        if k-1 == 0:
                            bug_lst.append((j, k-1, bug//2, 4))
                            continue
                        else:
                            bug_lst.append((j, k-1, bug, wasd))
 
                    elif wasd == 4:
                        if k+1 == N-1:
                            bug_lst.append((j, k+1, bug//2, 3))
                            continue
                        else:
                            bug_lst.append((j, k+1, bug, wasd))
 
        merged_cells = {}
        for new_y, new_x, bug_count, direction in bug_lst:
            pos = (new_y, new_x)
            if pos not in merged_cells:
                merged_cells[pos] = []
            merged_cells[pos].append((bug_count, direction))
        for (new_y, new_x), bugs_in_cell in merged_cells.items():
            if len(bugs_in_cell) > 1:
                total_bug = sum(b[0] for b in bugs_in_cell)
                max_bug_cluster = max(bugs_in_cell, key=lambda b: b[0])
                final_direction = max_bug_cluster[1]
                lst[new_y][new_x] = (total_bug, final_direction)
            else:
                lst[new_y][new_x] = bugs_in_cell[0]
        func(cnt+1, lst)
    func(0, lst)
    print(f'#{tc} {result}')