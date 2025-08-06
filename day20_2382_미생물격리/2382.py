tc = int(input())
for h in range(1, tc+1):
    q,w,e = map(int, input().split())
    dir_wasd = { 1: (-1,0), 2:(1,0), 3:(0,-1), 4:(0,1) }
    bug_dic = {}
    for i in range(e):
        x,y,bug_cnt,wasd = map(int, input().split())
        bug_dic[i] = [x,y,bug_cnt,wasd]

    for _ in range(w):
        for i in bug_dic:
            cnt = 0
            for j in bug_dic[i]:
                if j is not None:
                    cnt += 1
                    if cnt == 4:
                        dx, dy = dir_wasd[j]
                        bug_dic[i][0] += dx
                        bug_dic[i][1] += dy

                        if bug_dic[i][0] == 0 or bug_dic[i][0] == q-1 or bug_dic[i][1] == 0 or bug_dic[i][1] == q-1:
                            bug_dic[i][2] = bug_dic[i][2] // 2
                            if bug_dic[i][3] == 1: bug_dic[i][3] = 2
                            elif bug_dic[i][3] == 2: bug_dic[i][3] = 1
                            elif bug_dic[i][3] == 3: bug_dic[i][3] = 4
                            elif bug_dic[i][3] == 4: bug_dic[i][3] = 3

        merged = {}
        for i in bug_dic:
            if bug_dic[i][0] is None: continue
            pos = (bug_dic[i][0], bug_dic[i][1])
            if pos not in merged:
                merged[pos] = []
            merged[pos].append(i)

        for pos in merged:
            ids = merged[pos]
            if len(ids) < 2:
                continue
            ids.sort(key=lambda x: bug_dic[x][2], reverse=True)
            survivor = ids[0]
            for other in ids[1:]:
                bug_dic[survivor][2] += bug_dic[other][2]
                bug_dic[other] = [None, None, None, None]

    result = 0
    for i in bug_dic:
        if bug_dic[i][2] is not None:
            result += bug_dic[i][2]
    print(f'#{h} {result}')
