TC = int(input())
for t in range(1, TC+1):
    N = int(input())
    lst_1 = list(map(int, input().split()))
    lst_2 = list(map(int, input().split()))
    count = 0
 
    for i in range(N):
        if lst_2[i] != lst_1[i]:
            count += 1
            if lst_2[i] == 0:
                for j in range(i, N):
                    if lst_1[j] == 0:
                        lst_1[j] = 1
                    else:
                        lst_1[j] = 0
            else:
                for j in range(i, N):
                    if lst_1[j] == 1:
                        lst_1[j] = 0
                    else:
                        lst_1[j] = 1
    print(f'#{t} {count}')
