N = int(input())
lst = list(map(int, input().split()))
 
dic = {}
for i in range(len(lst)-1):
    if i % 2 == 0:
        if dic.get(lst[i]) == None:
            dic[lst[i]] = [lst[i+1]]
        else:
            dic[lst[i]].append(lst[i+1])
result = [1]
result_2 = []
result_3 = []
 
def dfs(dic, dic_key):
    global visited, result
    if dic.get(dic_key) == None:
        return
    for i in dic[dic_key]:
        result.append(i)
        dfs(dic, i)
 
def mid_dfs(dic, dic_key):
    global visited, result_2
    if dic.get(dic_key) == None:
        result_2.append(dic_key)
        return
    idx = dic[dic_key]
    if len(idx) == 2:
        mid_dfs(dic, idx[0])
        result_2.append(dic_key)
        mid_dfs(dic, idx[1])
    else:
        mid_dfs(dic, idx[0])
        result_2.append(dic_key)
 
def right_dfs(dic, dic_key):
    global visited, result_3
    if dic.get(dic_key) == None:
        result_3.append(dic_key)
        return
    idx = dic[dic_key]
    if len(idx) == 2:
        right_dfs(dic, idx[0])
        right_dfs(dic, idx[1])
        result_3.append(dic_key)
    else:
        right_dfs(dic, idx[0])
        result_3.append(dic_key)
 
dfs(dic, 1)
mid_dfs(dic, 1)
right_dfs(dic, 1)
 
print(*result)
print(*result_2)
print(*result_3)