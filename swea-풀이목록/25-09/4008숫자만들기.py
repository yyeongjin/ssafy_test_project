T = int(input())
for tc in range(1, T+1):
    N = int(input())
    plus, minus, x, olo = map(int, input().split())
    lst = list(map(int, input().split()))
    max_result = float('-inf')
    min_result = float('inf')
    def dfs(total, plus, minus, x, olo, depth):
        global max_result, min_result
        if depth == N:
            max_result = max(max_result, int(total))
            min_result = min(min_result, int(total))
            return
        if plus > 0:
            dfs(total+lst[depth], plus-1, minus, x, olo, depth+1)
        if minus > 0:
            dfs(total-lst[depth], plus, minus-1, x, olo, depth+1)
        if x > 0:
            dfs(total*lst[depth], plus, minus, x-1, olo, depth+1)
        if olo > 0:
            dfs(int(total/lst[depth]), plus, minus, x, olo-1, depth+1)
 
    dfs(lst[0], plus, minus, x, olo, 1)
 
    print(f'#{tc} {abs(max_result-min_result)}')