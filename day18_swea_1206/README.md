# SWEA View. 1206 회고

## 1. 초기 구현

처음에는 `i` 인덱스를 기준으로 좌우 2칸 이내 건물들과의 높이를 직접 비교하여,  
가장 큰 값을 차감하는 방식으로 로직을 구성했다.

내장 함수 없이 조건문 위주로 비교를 진행했고, 코드 흐름은 다음과 같았다.

```python
for j in range(1, 11):
    a = int(input())
    lst = list(map(int, input().split()))
    result = 0
    for i in range(len(lst)):
        if i == 0 and lst[i] > lst[i+1] and lst[i] > lst[i+2]:
            if lst[i+1] > lst[i+2]:
                result += lst[i] - lst[i+1]
            else:
                result += lst[i] - lst[i+2]
        elif i == 1 and lst[i] > lst[i+1] and lst[i] > lst[i+2] and lst[i] > lst[i-1]:
            if lst[i+1] > lst[i+2] and lst[i-1]:
                result += lst[i] - lst[i+1]
            elif lst[i+2] > lst[i+1] and lst[i-1]:
                result += lst[i] - lst[i+2]
            elif lst[i-1] > lst[i+1] and lst[i+2]:
                result += lst[i] - lst[i-1]
        elif 1 < i and i+2 < len(lst):
            if lst[i] > lst[i+1] and lst[i] > lst[i+2] and lst[i] > lst[i-1] and lst[i] > lst[i-2]:
                if lst[i+1] > lst[i+2] and lst[i+1] > lst[i-1] and lst[i+1] > lst[i-2]:
                    result += lst[i] - lst[i+1]
                elif lst[i+2] > lst[i+1] and lst[i+2] > lst[i-1] and lst[i+2] > lst[i-2]:
                    result += lst[i] - lst[i+2]
                elif lst[i-1] > lst[i+2] and lst[i-1] > lst[i+1] and lst[i-1] > lst[i+2]:
                    result += lst[i] - lst[i-1]
                elif lst[i-2] > lst[i+2] and lst[i-2] > lst[i-1] and lst[i-2] > lst[i+1]:
                    result += lst[i] - lst[i-2]
    print(f'#{j} {result}')
```

하지만 결과적으로는 **문제를 정확히 풀지 못했다.**  
조건 분기나 비교 대상이 많아지면서 **로직이 복잡해지고, 오류 발생 가능성도 커졌다.**

---

## 2. `max()` 함수 활용 리팩토링

이후에는 `max()` 내장 함수를 적극적으로 활용하여 비교 대상을 묶었고,  
조건을 간결하게 개선했다.

```python
for j in range(1, 11):
    a = int(input())
    lst = list(map(int, input().split()))
    result = 0
    for i in range(len(lst)):
        if i == 0 and lst[i] > lst[i+1] and lst[i] > lst[i+2]:
            result += lst[i] - max(lst[i+1], lst[i+2])
        elif i == 1 and lst[i] > lst[i+1] and lst[i] > lst[i+2] and lst[i] > lst[i-1]:
            result += lst[i] - max(lst[i+1], lst[i+2], lst[i-1])
        elif 1 < i and i+2 < len(lst):
            if lst[i] > lst[i+1] and lst[i] > lst[i+2] and lst[i] > lst[i-1] and lst[i] > lst[i-2]:
                result += lst[i] - max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])
    print(f'#{j} {result}')
```

이 방식은 **가독성은 조금 향상되었지만**, 여전히 조건 분기와 인덱스 비교가 많아  
전체적인 구조가 복잡하고, 반복되는 패턴이 존재했다.

---

## 3. 개선이 필요한 지점

현재 구현된 코드에서 다음과 같은 개선점이 존재한다:

- **조건 분기 과다**  
  → `i` 값에 따른 예외 처리(0, 1 등)가 많아 코드 흐름이 복잡하다.

- **반복되는 로직**  
  → `if lst[i] > ...` 구조가 반복되며 유지보수가 어렵다.

- **비교 대상 관리 어려움**  
  → `lst[i±1]`, `lst[i±2]` 등 인덱스 비교가 많아지면서, 인덱스 범위 초과나 누락 등의 위험이 존재한다.

---

## 4. 다음 목표 및 개선 방향

- 반복되는 인덱스 조건을 **`range(2, len(lst)-2)`로 고정하고**,  
  **비교 대상들을 슬라이싱하여 처리**하는 구조로 개선할 수 있다.
  
- `max()`를 활용하되, **조건 분기는 최소화하고 일관성 있는 조건 처리**를 구성해야 한다.

- 반복 패턴이 보이는 부분은 함수화 또는 패턴화하여 **코드 길이와 난독성을 줄이는 방향**으로 리팩토링하는 것이 좋다.

---

## 회고 요약

- 처음엔 **하드코딩으로도 충분히 풀 수 있다고 생각했지만**, 인덱스 조건이 많아질수록 오히려 복잡성이 증가했다.  
- `max()` 함수 하나만으로도 **로직을 대폭 간소화**할 수 있다는 점을 경험했다.  
- **비슷한 조건이 반복되면 추상화하거나 슬라이싱을 고려하는 습관이 중요**하다는 점을 느꼈다.  
- 다음부터는 **설계 단계에서 전체적인 반복 구조를 먼저 파악한 후**, 예외 처리는 나중에 보강하는 방식으로 접근할 계획이다.
