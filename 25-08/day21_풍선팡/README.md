# SWEA 14510 - 풍선팡

## 문제 개요

격자판 위에 숫자가 적힌 풍선들이 있다. 한 칸을 선택하면 해당 칸에 적힌 숫자만큼 상하좌우 방향으로 풍선이 터지며 점수를 얻게 된다. 이때 가장 높은 점수를 얻을 수 있는 칸을 찾아, 그 점수를 출력하는 문제다.

## 입력 설명

- 첫 줄에 테스트 케이스의 수 `T`가 주어진다.
- 각 테스트 케이스는 다음과 같은 형식으로 주어진다:
  - 첫 줄: `M N` (행, 열)
  - 다음 `M`줄: 각 줄에 `N`개의 숫자

## 출력 설명

- 각 테스트 케이스마다 `#tc 최대점수` 형식으로 출력한다.

## 접근 방식

- 각 칸을 중심으로 상하좌우 4방향을 풍선의 숫자만큼 탐색하며 점수를 계산한다.
- 경계 조건이 다양하기 때문에, 위치별로 조건문을 분기하여 안전하게 탐색한다.
- 각 칸에서 얻을 수 있는 점수의 최댓값을 `result_lst`에 저장하고, 그 중 최댓값을 출력한다.

## 시간복잡도

- 각 칸마다 최대 `4 * n`번 탐색하므로, 전체 시간복잡도는 `O(M * N * K)` 수준이다.  
  (단, K는 한 칸의 최대 숫자 범위)
- 입력 범위가 작기 때문에 완전탐색으로도 충분히 통과 가능하다.

## 개선 방향

- 현재 구현은 위치마다 조건문으로 분기되어 있어 중복 코드가 많다.
- `dx`, `dy`를 이용한 방향 벡터 처리로 코드 압축이 가능하며, 가독성과 유지보수성도 향상된다.
- 점수 계산 로직을 함수로 분리하면 구조적으로 더 깔끔한 풀이가 된다.

## 회고

이번 문제는 조건 분기와 완전 탐색 구현 연습에 적합한 문제였다.  
단순한 탐색 문제처럼 보이지만, 가장자리 / 코너 / 내부 등 위치에 따라 탐색 방향이 달라지기 때문에 조건 처리에 신경을 많이 써야 했다.

문제 풀이 과정에서 반복되는 코드가 많았고, 이를 줄이기 위한 구조화가 아쉬웠다.  
특히, 하나의 기준 칸에 대해 상하좌우를 동일한 패턴으로 탐색하는 구조는 일반화가 충분히 가능한데도, 각 조건을 하드코딩한 점은 개선 여지가 있다.

다만 목표였던 **정확한 구현** 자체는 성공적으로 달성했고, 경계값 처리에 대한 감각을 기를 수 있었다.  
다음에는 같은 문제를 더 간결하게 풀 수 있는 설계 관점에서 접근해보고 싶다.

## 코드
~~~python
tc = int(input())
for h in range(1, tc+1):
    M,N = map(int, input().split())
    lst = []
    for i in range(M):
        lst.append(list(map(int, input().split())))

    result_lst = []
    for i in range(M):
        for j in range(N):
            result = 0
            if i == 0 and j == 0:
                result += lst[i][j]
                for k in range(1, lst[i][j]+1):
                    if i+k < M:
                        result += lst[i+k][j]
                for k in range(1, lst[i][j]+1):
                    if j+k < N:
                        result += lst[i][j+k]
                result_lst.append(result)

            elif i == M-1 and j == N-1:
                result += lst[i][j]
                for k in range(1, lst[i][j]+1):
                    if i-k >= 0:
                        result += lst[i-k][j]
                for k in range(1, lst[i][j]+1):
                    if j-k >= 0:
                        result += lst[i][j-k]
                result_lst.append(result)

            elif i == M-1 and j == 0:
                result += lst[i][j]
                for k in range(1, lst[i][j]+1):
                    if i-k >= 0:
                        result += lst[i-k][j]
                for k in range(1, lst[i][j]+1):
                    if j+k < N:
                        result += lst[i][j+k]
                result_lst.append(result)

            elif i == 0 and j == N-1:
                result += lst[i][j]
                for k in range(1, lst[i][j]+1):
                    if i+k < M:
                        result += lst[i+k][j]
                for k in range(1, lst[i][j]+1):
                    if j-k >= 0:
                        result += lst[i][j-k]
                result_lst.append(result)

            elif i == 0:
                result += lst[i][j]
                for k in range(1, lst[i][j]+1):
                    if i+k < M:
                        result += lst[i+k][j]
                for k in range(1, lst[i][j]+1):
                    if j+k < N:
                        result += lst[i][j+k]
                for k in range(1, lst[i][j]+1):
                    if j-k >= 0:
                        result += lst[i][j-k]
                result_lst.append(result)

            elif j == 0:
                result += lst[i][j]
                for k in range(1, lst[i][j]+1):
                    if i+k < M:
                        result += lst[i+k][j]
                for k in range(1, lst[i][j]+1):
                    if i-k >= 0:
                        result += lst[i-k][j]
                for k in range(1, lst[i][j]+1):
                    if j+k < N:
                        result += lst[i][j+k]
                result_lst.append(result)

            elif i == M-1:
                result += lst[i][j]
                for k in range(1, lst[i][j]+1):
                    if i-k >= 0:
                        result += lst[i-k][j]
                for k in range(1, lst[i][j]+1):
                    if j+k < N:
                        result += lst[i][j+k]
                for k in range(1, lst[i][j]+1):
                    if j-k >= 0:
                        result += lst[i][j-k]
                result_lst.append(result)

            elif j == N-1:
                result += lst[i][j]
                for k in range(1, lst[i][j]+1):
                    if i+k < M:
                        result += lst[i+k][j]
                for k in range(1, lst[i][j]+1):
                    if i-k >= 0:
                        result += lst[i-k][j]
                for k in range(1, lst[i][j]+1):
                    if j-k >= 0:
                        result += lst[i][j-k]
                result_lst.append(result)

            else:
                result += lst[i][j]
                for k in range(1, lst[i][j]+1):
                    if i+k < M:
                        result += lst[i+k][j]
                for k in range(1, lst[i][j]+1):
                    if i-k >= 0:
                        result += lst[i-k][j]
                for k in range(1, lst[i][j]+1):
                    if j-k >= 0:
                        result += lst[i][j-k]
                for k in range(1, lst[i][j]+1):
                    if j+k < N:
                        result += lst[i][j+k]
                result_lst.append(result)
    print(f'#{h} {max(result_lst)}')
~~~
