T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = []
    dic = {}
    for i in range(N):
        value = list(input().split())
        if dic.get(value[0]) == None:
            dic[value[0]] = value[1::]
 
    def dfs(dic, key):
        if len(dic[key]) == 1:
            return int(dic[key][0])
        operator, left, right = dic[key]
        left_value = dfs(dic, left)
        right_value = dfs(dic, right)
        if operator == "*":
            return left_value * right_value
        elif operator == "/":
            return left_value // right_value
        elif operator == "-":
            return left_value - right_value
        elif operator == "+":
            return left_value + right_value
 
    print(f'#{tc} {dfs(dic, "1")}')