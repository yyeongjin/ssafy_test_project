T = int(input())
for tc in range(1, T+1):
    init_lst = list(map(int, input().split()))
    num = list(map(int, str(init_lst[0]).strip()))
    count = init_lst[1]
    result = 0
    visited = set()
    def dfs(num_lst, cnt):
        global result
        if (cnt, str(num_lst)) not in visited:
            visited.add((cnt, str(num_lst)))
        else:
            return
        if cnt == count:
            res = int("".join(map(str, num_lst)))
            if res > result:
                result = res
            return
        cnt_1 = len(num_lst)
        for i in range(cnt_1 - 1):
            for j in range(i + 1, cnt_1):
                num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
                dfs(num_lst, cnt + 1)
                num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
 
    dfs(num, 0)
    print(f'#{tc} {result}')