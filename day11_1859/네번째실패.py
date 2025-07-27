a = int(input())
  
for i in range(1, a+1):
    b = int(input())
    c = list(map(int, input().split()))
    d = c[:]
    c.sort()
    count = 0
    result_1 = 0
    result_2 = 0
    for j in range(len(d)):
        if c[-1] == d[j]:
            if result_1 == 0:
                c.pop()
                continue
            result_2 += (int(c.pop()) * (count)) - result_1
            result_1 = 0
            count = 0
            if len(c) == 0:
                break
        else:
            count += 1
            result_1 += d[j]
    print("#"+str(i), str(result_2))