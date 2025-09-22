T = int(input())
for tc in range(1, T+1):
    from collections import deque
    K = int(input())
    fr_lst = deque(map(int, input().split()))
    se_lst = deque(map(int, input().split()))
    th_lst = deque(map(int, input().split()))
    fo_lst = deque(map(int, input().split()))
    for _ in range(K):
        stone, turn = map(int, input().split())
        fr_se_diff = fr_lst[2] != se_lst[6]
        se_th_diff = se_lst[2] != th_lst[6]
        th_fo_diff = th_lst[2] != fo_lst[6]
        if stone == 1:
            if turn == 1: fr_lst.appendleft(fr_lst.pop())
            else: fr_lst.append(fr_lst.popleft())
            if fr_se_diff:
                if turn == 1: se_lst.append(se_lst.popleft())
                else: se_lst.appendleft(se_lst.pop())
                if se_th_diff:
                    if turn == 1: th_lst.appendleft(th_lst.pop())
                    else: th_lst.append(th_lst.popleft())
                    if th_fo_diff:
                        if turn == 1: fo_lst.append(fo_lst.popleft())
                        else: fo_lst.appendleft(fo_lst.pop())
        elif stone == 2:
            if turn == 1: se_lst.appendleft(se_lst.pop())
            else: se_lst.append(se_lst.popleft())
            if fr_se_diff:
                if turn == 1: fr_lst.append(fr_lst.popleft())
                else: fr_lst.appendleft(fr_lst.pop())
            if se_th_diff:
                if turn == 1: th_lst.append(th_lst.popleft())
                else: th_lst.appendleft(th_lst.pop())
                if th_fo_diff:
                    if turn == 1: fo_lst.appendleft(fo_lst.pop())
                    else: fo_lst.append(fo_lst.popleft())
        elif stone == 3:
            if turn == 1: th_lst.appendleft(th_lst.pop())
            else: th_lst.append(th_lst.popleft())
            if th_fo_diff:
                if turn == 1: fo_lst.append(fo_lst.popleft())
                else: fo_lst.appendleft(fo_lst.pop())
            if se_th_diff:
                if turn == 1: se_lst.append(se_lst.popleft())
                else: se_lst.appendleft(se_lst.pop())
                if fr_se_diff:
                    if turn == 1: fr_lst.appendleft(fr_lst.pop())
                    else: fr_lst.append(fr_lst.popleft())
        elif stone == 4:
            if turn == 1: fo_lst.appendleft(fo_lst.pop())
            else: fo_lst.append(fo_lst.popleft())
            if th_fo_diff:
                if turn == 1: th_lst.append(th_lst.popleft())
                else: th_lst.appendleft(th_lst.pop())
                if se_th_diff:
                    if turn == 1: se_lst.appendleft(se_lst.pop())
                    else: se_lst.append(se_lst.popleft())
                    if fr_se_diff:
                        if turn == 1: fr_lst.append(fr_lst.popleft())
                        else: fr_lst.appendleft(fr_lst.pop())
    result = 0
    if fr_lst[0] == 1:
        result += 1
    if se_lst[0] == 1:
        result += 2
    if th_lst[0] == 1:
        result += 4
    if fo_lst[0] == 1:
        result += 8
    print(f'#{tc} {result}')
