# SWEA 2382. 미생물 격리

## 문제 요약

- 정사각형 모양의 셀 격자 안에서 여러 개의 미생물 군집이 이동한다.
- 각 군집은 방향을 가지고 있으며, 한 칸씩 이동한다.
- 격자의 가장자리에 도달하면 미생물 수가 절반으로 줄고 방향이 반전된다.
- 이동한 뒤 같은 셀에 도달한 군집이 여러 개라면, 가장 많은 미생물 수를 가진 군집 하나만 남고 나머지는 합쳐진다.
- 주어진 시간 동안 모든 이동을 마친 후, 남아 있는 미생물 수의 총합을 구하는 문제다.

---

## 내가 작성한 코드

```python
from collections import defaultdict
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
                    if cnt == 4: # 좌표
                        x,y = dir_wasd[j]
                        if bug_dic[i][0] != 0: # x좌표가 0이 아닐 경우
                            bug_dic[i][0] += x
                            if bug_dic[i][0] == 0: # x만큼 더했을 때 0이 된 경우
                                bug_dic[i][2] = bug_dic[i][2] // 2 # 벌레 절반만 남김
                                if bug_dic[i][3] == 1: # 좌표가 1일 경우
                                    bug_dic[i][3] = 2 
                                elif bug_dic[i][3] == 2: # 좌표가 2일 경우
                                    bug_dic[i][3] = 1

                        if bug_dic[i][1] != 0: # y 좌표가 0이 아닐 경우
                            bug_dic[i][1] += y
                            if bug_dic[i][1] == 0: # y만큼 더했을 때 0이 된 경우
                                bug_dic[i][2] = bug_dic[i][2] // 2 # 벌레 절반만 남김
                                if bug_dic[i][3] == 3: # 좌표가 3일 경우
                                    bug_dic[i][3] = 4
                                elif bug_dic[i][3] == 4: # 좌표가 4일 경우
                                    bug_dic[i][3] = 3


            """개선 필요 로직
            for j in list(bug_dic.keys()):          # 벌레 좌표 조회
                for k in list(bug_dic.keys()):      # 벌레 좌표 조회
                    if j >= k:                      # 불필요한 연산 x (이미 비교한 경우)
                        continue
                    if bug_dic[j][0] is not None and bug_dic[k][0] is not None:
                        if bug_dic[j][0] == bug_dic[k][0] and bug_dic[j][1] == bug_dic[k][1]:
                            if bug_dic[j][2] >= bug_dic[k][2]:
                                bug_dic[j][2] += bug_dic[k][2]
                                bug_dic[k][0] = None
                                bug_dic[k][1] = None
                                bug_dic[k][2] = None
                                bug_dic[k][3] = None
                            elif bug_dic[k][2] >= bug_dic[j][2]:
                                bug_dic[k][2] += bug_dic[j][2]
                                bug_dic[j][0] = None
                                bug_dic[j][1] = None
                                bug_dic[j][2] = None
                                bug_dic[j][3] = None
            """
                                
    result = 0
    for i in bug_dic:
        if bug_dic[i][2] is not None:
            result += bug_dic[i][2]
    print(f'#{h} {result}')
```

## 회고

현재 코드에서는 미생물의 이동과 가장자리에 도달했을 때 수가 절반으로 줄고 방향이 반전되는 처리까지는 직접 구현했고,  
이 부분은 비교적 정확하게 동작한다고 판단했다.  
하지만 여러 군집이 동시에 같은 위치에 도달했을 때의 병합 처리는 아직 완성하지 못했다.

특히 3개 이상의 군집이 동일한 위치로 이동한 경우,  
내가 작성한 병합 로직은 두 개씩만 비교하며 병합을 처리하는 방식이라  
정확한 규칙을 만족하지 못했고, 결과도 정답과 일치하지 않았다.

이 과정에서 GPT를 통해  
**"같은 위치에 모인 미생물 군집 중, 가장 많은 수를 가진 군집만 남기고 나머지를 모두 합친다"**는 정확한 병합 규칙을 이해하게 되었고,  
어떤 방식으로 구현해야 하는지도 파악할 수 있었다.

아직 내 코드에는 그 병합 로직이 제대로 적용되지 않았지만,  
문제 해결 방법과 원리를 이해했기 때문에  
**다음에는 병합 로직까지도 스스로 완성시켜 올바른 정답을 도출할 수 있도록 다시 구현해볼 계획이다.**

---

## 다음에 다시 풀면?

여러 개체가 동일한 위치로 이동할 수 있는 시뮬레이션 문제에서는  
**모든 이동이 끝난 뒤, 좌표 기준으로 병합 대상을 정리하고, 가장 큰 군집 하나만 남기고 나머지를 병합하는 방식이 가장 안정적이고 논리적인 처리 방식**이라는 점을 배웠다.

또한 조건이 많고 상태 변화가 복잡한 문제일수록  
**각 단계를 나눠서 처리하고, 상태를 실시간으로 변경하기보다는 중간 결과를 임시로 저장하여 일괄 처리하는 구조가 훨씬 안정적**이라는 것도 체감할 수 있었다.
