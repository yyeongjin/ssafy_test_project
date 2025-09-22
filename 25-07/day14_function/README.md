# 함수 및 모듈 개요 정리

## 1. 함수 (Functions)

- 함수는 재사용 가능한 코드 블록
- 정의: `def 함수이름(매개변수):`
- 호출: `함수이름(인자)`
- 구조: 매개변수 / Docstring / 본문 / 반환값
- 매개변수(parameter): 정의할 때 사용
- 인자(argument): 호출할 때 넘김
- 인자 종류:
  - 위치 인자
  - 기본값 인자
  - 키워드 인자
  - *args
  - **kwargs

### 예시
```python
def get_sum(a, b):
    """두 수의 합을 반환"""
    return a + b

result = get_sum(3, 5)
```

## 2. Scope (LEGB Rule)

- Local > Enclosed > Global > Built-in
- 함수 내에서 외부 변수 수정하려면 global, nonlocal 필요

## 3. 재귀 함수

- 자기 자신 호출
- 종료 조건 필수

### 팩토리얼 예시
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

## 4. 내장 함수

- `len()`, `max()`, `sum()`, `sorted()`, `map()`, `zip()`

### map 예시
```python
numbers = [1, 2, 3]
result = list(map(str, numbers))
```

### zip 예시
```python
a = [1, 2]
b = ['A', 'B']
pair = list(zip(a, b))
```

## 5. 함수 스타일 가이드

- 소문자 + 언더스코어 사용
- 동사 + 명사
- 하나의 함수는 하나의 책임만 (SRP)
- 예시:
  - `validate_password()`
  - `save_user()`
  - `send_email()`

## 6. 패킹 & 언패킹

### 패킹
```python
a = 1, 2, 3
```

### 언패킹
```python
x, y, z = a
```

### 함수 인자 언패킹
```python
def func(x, y): pass

args = (1, 2)
kwargs = {'x': 1, 'y': 2}
func(*args)
func(**kwargs)
```

## 7. 모듈

- `.py` 파일 = 모듈
- `import` 또는 `from ... import ...` 사용
- `as`로 별칭 가능

### 내장 모듈 예시
```python
import math
print(math.sqrt(4))
print(math.pi)
```

### 사용자 정의 모듈 예시
```python
# my_math.py
def add(a, b):
    return a + b

# main.py
import my_math
my_math.add(1, 2)
```

## 8. 패키지

- 디렉토리 + `__init__.py` = 패키지
- `from my_package.math import add` 방식으로 사용

### 구조 예시
```
my_package/
│
├── __init__.py
├── math.py
└── tools.py
```

## 9. 외부 패키지

- 설치: `pip install 패키지명`
- 예시:
```bash
pip install requests
```

## 10. 람다

- 익명 함수
```python
addition = lambda x, y: x + y
```

- map과 함께 사용
```python
squared = list(map(lambda x: x**2, [1, 2, 3]))
```

## 11. help()

- 모듈 내부 확인 가능
```python
import math
help(math)
```
