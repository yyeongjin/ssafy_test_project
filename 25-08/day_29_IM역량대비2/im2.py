T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    init_num = 0
    result_lst = []
    lst.sort()
 
    for i in range(N):
        count = 0
        for j in range(i, N):
            if j == i:
                init_num = int(lst[j])
            if lst[j] - init_num <= K:
                count += 1
            else:
                result_lst.append(count)
                break
            result_lst.append(count)
             
    print(f'#{tc} {max(result_lst)}')
