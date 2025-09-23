T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    dic = {}
    for i in range(len(lst)):
        dic[i] = [(lst[i][0] * 2 + 2000, lst[i][1] * 2 + 2000), (lst[i][2], lst[i][3])]
    result = 0
 
    while True:
        next_count = {}
        for i in range(len(lst)):
            x, y = dic[i][0]
            turn, count = dic[i][1]
 
            if count != 0:
                if turn == 0:
                    dx, dy = x, y + 1
                elif turn == 1:
                    dx, dy = x, y - 1
                elif turn == 2:
                    dx, dy = x - 1, y
                elif turn == 3:
                    dx, dy = x + 1, y
 
                if 0 <= dx <= 4000 and 0 <= dy <= 4000:
                    if (dx, dy) not in next_count:
                        next_count[(dx, dy)] = []
                    next_count[(dx, dy)].append(i)
                else:
                    dic[i][1] = (turn, 0)
 
        temp_set = set()
        for wasd, idx in next_count.items():
            if len(idx) > 1:
                for i in idx:
                    temp_set.add(i)
            else:
                i = idx[0]
                dic[i][0] = wasd
 
        for i in temp_set:
            turn, count = dic[i][1]
            if count > 0:
                result += count
                dic[i][1] = (turn, 0)
 
        cnt = 0
        for i in range(len(lst)):
            if dic[i][1][1] == 0:
                cnt += 1
 
        if cnt == len(lst):
            break
 
    print(f'#{tc} {result}')