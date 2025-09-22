T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    dic = {i+1:0 for i in range(N)}
    for i in range(M):
        dic_key, dic_value = map(int, input().split())
        dic[dic_key] = dic_value
 
    grape_dic = {}
    for i in range(1, N//2+1):
        if 2*i+1 <= N:
            grape_dic[i] = [2*i, 2*i+1]
        else:
            grape_dic[i] = [2*i]
    result = 0
    def dfs(grape_dic, key):
        global result
        if grape_dic.get(key) == None:
            result += dic[key]
            return
        for i in grape_dic[key]:
            dfs(grape_dic, i)
 
    dfs(grape_dic, L)
    print(f"#{tc} {result}")