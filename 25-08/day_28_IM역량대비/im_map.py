T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [input().split() for _ in range(N)]
    wasd = [(1,0), (0,1), (-1,0), (0,-1)]
  
    max_num = 0
    idx_lst = []
  
    result_lst = []
  
    for i in range(N):
        for j in range(N):
            if max_num <= int(lst[i][j]):
                max_num = int(lst[i][j])
                idx_lst.append((max_num, i, j))
     
    for idx_num, x, y in idx_lst:
        if idx_num == max_num:
            v_lst = []
            v_lst.append(max_num)
            while True:
                min_idx = 1001
                for dx,dy in wasd:
                    nx, ny = dx+x, dy+y
                    if 0 <= nx < N and 0 <= ny < N:
                        if min_idx >= int(lst[nx][ny]):
                            min_idx = int(lst[nx][ny])
                            m_nx = nx
                            m_ny = ny
                    else:
                        continue
                if min_idx == 1001:
                    break
                if int(v_lst[-1]) <= min_idx:
                    break
                else:
                    x, y = m_nx, m_ny
                    v_lst.append(min_idx)
            result_lst.append(len(v_lst))
        else:
            continue
     
    print(f'#{tc} {max(result_lst)}')
