# 별찍기 - 10 회고

## 1. 함수 정의 및 초기 시도

가장 처음엔 `star(n, text)`라는 함수로 시작했다.  
기본적으로 `n == 1`일 때 단일 문자열을 리턴하고, 그 외에는 `result` 문자열을 조작하여 출력 형태를 구성했다.

```python
def star(n, text):
    if n == 1:
        return text
    result = ""
    star(n//3, text)
    for i in range(n//3):
        result += "*"*3
    result += "\n"
    for i in range(n//3):
        result += "*" + " "*(n//3) + "*"
    result += "\n"
    for i in range(n//3):
        result += "*"*3
    return result

print(star(3, "*"))
```

3일 때는 원하는 출력이 잘 되었지만,  
9 이상부터는 문자열 처리에 한계가 있었고,  
이스케이프 문자나 공백 처리가 복잡해지면서 관리가 어려워졌다.

---

## 2. 리스트 기반 재설계

문자열 기반 한계를 극복하기 위해 리스트 기반으로 코드를 다시 설계했다.  
이렇게 하면 줄바꿈 처리를 명확하게 할 수 있었다.

```python
def star(n, lst):
    if n == 1:
        return lst
    star(n//3, lst)
    result = []
    for i in range(n//3):
        result.append(lst[i]*3)
    for i in range(n//3):
        result.append(lst[i] + " "*(n//3) + lst[i])
    for i in range(n//3):
        result.append(lst[i]*3)
    return result

print(star(3, "*"))
```

이때 출력값은 다음과 같다.

```python
['***', '* *', '***']
```

줄바꿈 없이 리스트 단위로 출력되기 때문에,  
이를 시각적으로 확인하기 위해 `print()` 대신 **인덱스별 출력**이 필요하다는 점을 깨달았다.

---

## 3. 중첩 호출 실험과 깨달음

한 번에 큰 사이즈를 보기 위해 다음과 같이 중첩 호출을 시도해봤다.

```python
print(star(9, star(3, "*")))
```

출력값은 아래와 같았다.

```python
['*********', '* ** ** *', '*********',
 '***   ***', '* *   * *', '***   ***',
 '*********', '* ** ** *', '*********']
```

처음에는 출력이 이상하게 보였지만,  
사실 각 인덱스를 한 줄씩 출력해보면 **별의 모양이 정확하게 나오는 구조**라는 걸 확인할 수 있었다.

즉, 문자열 전체 출력이 아닌 리스트 요소별 `print()`를 해야 시각적으로 별 형태가 나온다는 점을 이때 깨달았다.

---

## 4. 에러 발생과 원인 분석

이전 코드에서 다음과 같은 실수를 했다.

```python
def star(n, lst):
    if n == 1:
        return lst
    star(n//3, lst)  # 반환값을 안 받음
    result = []
    for i in range(n//3):
        result.append(lst[i]*3)
    ...
```

위 코드에선 `lst = star(n//3, lst)`처럼  
**재귀의 반환값을 받지 않아서** `lst`가 갱신되지 않았고,  
그로 인해 `IndexError`가 발생했다는 점을 깨달았다.

---

## 5. 반환값 처리 개선 및 최종 구조

문제를 해결하기 위해 `lst = star(n//3, lst)`로 수정했고,  
이후에는 예상대로 잘 작동했다.

```python
def star(n, lst):
    if n == 1:
        return lst
    lst = star(n//3, lst)
    result = []
    for i in range(n//3):
        result.append(lst[i]*3)
    for i in range(n//3):
        result.append(lst[i] + " "*(n//3) + lst[i])
    for i in range(n//3):
        result.append(lst[i]*3)
    return result

print(star(9, "*"))
```

---

## 6. 사용자 입력과 전체 출력 구성

마지막으로 숫자 입력을 받을 수 있도록 구성했고,  
리스트 요소를 한 줄씩 출력하여 정돈된 결과를 얻었다.

```python
import sys
input = sys.stdin.readline

a = int(input())

def star(n, lst):
    if n == 1:
        return lst
    lst = star(n//3, lst)
    result = []
    for i in range(n//3):
        result.append(lst[i]*3)
    for i in range(n//3):
        result.append(lst[i] + " "*(n//3) + lst[i])
    for i in range(n//3):
        result.append(lst[i]*3)
    return result

result = star(a, ["*"])

for line in result:
    print(line)
```

---

## 회고 요약

- 문자열 기반보다는 리스트 기반 출력이 훨씬 직관적이었다.
- 재귀 함수는 **반환값을 반드시 받아야 하며**, 그렇지 않으면 기존 데이터가 그대로 남는다.
- `print(star(9, star(3, "*")))`처럼 중첩 호출도 가능하지만, 시각적 확인을 위해선 **리스트를 한 줄씩 출력해야 한다**.
- 재귀적인 구조를 상상하면서 구현하는 것이 처음엔 어렵지만, 하위 결과를 반복적으로 조합한다는 개념을 이해하고 나면 굉장히 유연하게 설계할 수 있다는 점을 배웠다.
