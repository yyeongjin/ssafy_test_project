a = int(input())
   
for i in range(1, a+1):
    b = int(input())
    c = list(map(int, input().split()))
    max = c[-1]
    result = 0
    for j in reversed(range(len(c))):
        if max > c[j]:
            result += max - c[j]
        else:
            max = c[j]
    print(f"#{i} {result}")