## 1. 개요
`itertools.permutations` 는 파이썬 표준 라이브러리 `itertools` 모듈에 포함된 함수로, **주어진 iterable(반복 가능한 객체)에서 가능한 모든 순열(permutation)을 생성**한다.  
순열은 원소의 순서를 고려하여 나열하는 경우의 수를 의미한다.  

---

## 2. 기본 사용법
```python
from itertools import permutations

permutations(iterable, r=None)
```

- **iterable**: 순열을 만들 원소들이 들어 있는 반복 가능한 객체 (list, tuple, string 등)  
- **r**: 뽑을 원소의 개수 (기본값은 `None`, 이 경우 iterable의 길이와 동일하게 뽑음)

---

## 3. 예제

### (1) 기본 순열
```python
from itertools import permutations

lst = [1, 2, 3]
result = permutations(lst)  # r 지정 안 하면 전체 길이만큼
print(list(result))
```

출력:
```
[(1, 2, 3), (1, 3, 2),
 (2, 1, 3), (2, 3, 1),
 (3, 1, 2), (3, 2, 1)]
```

---

### (2) 원소 개수를 제한한 순열
```python
from itertools import permutations

lst = ['a', 'b', 'c']
result = permutations(lst, 2)  # 2개씩만 뽑는 순열
print(list(result))
```

출력:
```
[('a', 'b'), ('a', 'c'),
 ('b', 'a'), ('b', 'c'),
 ('c', 'a'), ('c', 'b')]
```

---

## 4. 특징
- 반환 값은 **iterator** 객체이다. 따라서 결과를 직접 확인하려면 `list()`로 변환해야 한다.  
- 각 순열은 **tuple** 형태로 반환된다.  
- 중복 원소가 있는 경우, 중복된 원소를 구분하여 취급한다. (중복된 순열이 생길 수 있음)  
- 시간복잡도는 원소 수에 따라 매우 커질 수 있다. (n! / (n-r)!)  

---

## 5. 활용 예시
- 가능한 모든 암호 조합 테스트  
- 카드 섞기 시뮬레이션  
- 게임에서 가능한 모든 이동 순서 탐색  
- 특정 조건(합, 곱 등)에 맞는 조합 찾기  

---

## 6. 정리
- `itertools.permutations` 는 순열을 쉽게 생성할 수 있는 함수다.  
- `r`을 지정하지 않으면 전체 길이의 순열, 지정하면 `r`개 원소를 뽑는 순열을 생성한다.  
- 결과는 tuple들의 iterator이며, 필요 시 list로 변환해 사용한다.  
- 원소 수가 커질수록 경우의 수가 기하급수적으로 증가한다는 점에 주의해야 한다.  
