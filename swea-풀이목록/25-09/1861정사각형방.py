tc = int(input())
for t in range(1, tc+1):
    a = int(input())
    init_lst = []
    for _ in range(a):
        lst = list(map(int, input().split()))
        init_lst.append(lst)
    wasd = [(0,1), (1,0), (-1,0), (0,-1)]
    result = 0
    result_dic = {}
    result_cnt = 0
    for i in range(a):
        for j in range(a):
            for dx, dy in wasd:
                nx, ny = dx+i, dy+j
                if 0 <= nx < a and 0 <= ny < a:
                    if init_lst[i][j] + 1 == init_lst[nx][ny]:
                        result_dic[init_lst[i][j]] = [init_lst[nx][ny]]
                        break
 
    def dfs(dic, cnt , key):
        global result
        if dic.get(key) == None:
            if result < cnt:
                result = cnt
            return
        for i in dic[key]:
            dfs(dic, cnt+1, i)
 
    key_lst = []
    for i in result_dic.keys():
        key_lst.append(i)
    key_lst.sort()
 
    for i in key_lst:
        init_result = result
        dfs(result_dic, 1, i)
        if result != init_result:
            result_cnt = i
 
    print(f'#{t} {result_cnt} {result}')