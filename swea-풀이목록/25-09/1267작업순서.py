T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    lst = list(map(int, input().split()))
    dic = {}
    for i in range(len(lst)):
        if i % 2 == 0:
            if dic.get(lst[i]) == None:
                dic[lst[i]] = [ lst[i+1] ]
            else:
                dic[lst[i]].append(lst[i+1])
 
    result_dic = {i:0 for i in range(1, V+1)}
    def dfs(dic, dic_key):
        global result_dic
        if dic.get(dic_key) == None:
            return
        for i in dic[dic_key]:
            result_dic[i] = result_dic[i]+1
            dfs(dic, i)
 
    for i in range(1, V+1):
        dfs(dic, i)
 
    result_lst = list(result_dic.items())
    result_lst.sort(key=lambda x:x[1])
    result = ""
 
    for key, value in result_lst:
        result += str(key)+" "
    print(f'#{tc} {result}')