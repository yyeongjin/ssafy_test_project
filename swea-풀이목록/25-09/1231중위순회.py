T = 10
for tc in range(1, T+1):
    N = int(input())
    dic = {}
    for i in range(N):
        lst = list(input().split())
        dic[int(lst[0])] = lst[1]
    dic_1 = {}
    for i in range(1, N//2+1):
        if i*2 < N:
            dic_1[i] = [i*2, i*2+1]
        else:
            dic_1[i] = [i * 2]
    result = []
    def dfs(dic_1, key):
        if dic_1.get(key) == None:
            return result.append(dic[key])
        if len(dic_1[key]) == 2:
            value = dic_1[key]
            dfs(dic_1, value[0])
            result.append(dic[key])
            dfs(dic_1, value[1])
 
        else:
            value = dic_1[key]
            dfs(dic_1, value[0])
            result.append(dic[key])
 
    dfs(dic_1, 1)
    result_txt = "".join(result)
    print(f'#{tc} {result_txt}')