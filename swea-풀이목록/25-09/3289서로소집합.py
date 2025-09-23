def make_set(x):
    p[x] = x
 
 
def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]
 
 
def union(x, y):
    px = find_set(x)
    py = find_set(y)
 
    if px != py:
        if px < py:
            p[py] = px
        else:
            p[px] = py
 
 
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    p = [0] * (N + 1)
 
    for i in range(1, N + 1):
        make_set(i)
 
    result = ""
    for i in range(M):
        count, a, b = map(int, input().split())
        if count == 0:
            union(a, b)
        elif count == 1:
            if find_set(a) == find_set(b):
                result += '1'
            else:
                result += '0'
 
    print(f'#{tc} {result}')