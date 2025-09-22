# DFS와 BFS 구현

이 코드는 주어진 그래프를 입력받아 **DFS(깊이 우선 탐색)**과 **BFS(너비 우선 탐색)**을 수행하는 프로그램이다.  
그래프는 인접 리스트(딕셔너리) 형태로 저장되며, 시작 노드에서의 탐색 결과를 출력한다.

---

## 코드 설명

- `dfs_lst`, `bfs_lst` : 방문 여부를 저장하는 리스트
- `dic` : 그래프의 인접 리스트 (양방향 그래프)
- `dfs(num)` : 깊이 우선 탐색(재귀)
- `bfs(num)` : 너비 우선 탐색(큐, deque 활용)

DFS는 **재귀** 방식으로 구현되었고, BFS는 **큐(deque)**를 이용하여 구현되었다.  
각 탐색 결과는 문자열(`result`, `result_2`)에 공백으로 구분되어 저장되며, 출력 시 사용된다.

---

## 전체 코드

```python
from collections import deque
import sys
sys.setrecursionlimit(1_000_000)
N,M,V = map(int, input().split())

dfs_lst = [False] * (N+1)
bfs_lst = [False] * (N+1)

dic = {}
for i in range(M):
    x,y = map(int, input().split())
    if dic.get(x) == None:
        dic[x] = [y]
    else:
        dic[x].append(y)
    if dic.get(y) == None:
        dic[y] = [x]
    else:
        dic[y].append(x)

for k in dic:
    dic[k].sort() 

result = ""
def dfs(num):
    global result
    if not dic.get(num):
        return
    if dfs_lst[num] == False:
        dfs_lst[num] = True
        result += str(num) +" "
    for i in dic[num]:
        if dfs_lst[i] == False:
            dfs(i)

result_2 = ""
def bfs(num):
    global result_2
    if not dic.get(num):
        return
    q = deque([num])
    bfs_lst[num] = True
    while q:
        cnt = q.popleft()
        result_2 += str(cnt) + " "
        for i in dic.get(cnt, []):
            if bfs_lst[i] == False:
                bfs_lst[i] = True
                q.append(i)

dfs(V)
bfs(V)
if not result:
    print(V)
else:
    print(result)
if not result_2:
    print(V)
else:
    print(result_2)
```

---

## 특징 및 장점

- DFS는 **재귀**를 사용하여 간결하게 구현한다  
- BFS는 **deque**를 이용해 효율적으로 탐색한다  
- 방문 순서를 보장하기 위해 각 정점의 인접 리스트를 **정렬**하여 관리한다  
