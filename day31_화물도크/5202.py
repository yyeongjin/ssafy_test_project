T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s_e_lst = [tuple(map(int, input().split())) for _ in range(N)]
    s_e_lst.sort(key=lambda x: x[1])
     
    init = 0
    count = 0
    for x, y in s_e_lst:
        if init <= x:
            init = y
            count += 1
 
    print(f"#{tc} {count}")
