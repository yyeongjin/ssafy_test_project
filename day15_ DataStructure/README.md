## 1. 문자열 (String)

불변 객체  
메서드 실행 시 새로운 문자열 반환

- find(x)
- index(x)
- replace(a, b)
- strip()
- split(delim)
- join(iterable)

```python
text = " Hello, Python "
text.find("o")
text.index("o")
text.replace("Python", "World")
text.strip()
text.split(",")
",".join(["a", "b", "c"])
```

---

## 2. 리스트 (List)

가변 객체  
값 직접 변경 가능

- append(x)
- extend(iter)
- insert(i, x)
- remove(x)
- pop(i)
- index(x)
- count(x)
- reverse()
- sort()

```python
lst = [1, 2, 3]
lst.append(4)
lst.extend([5, 6])
lst.insert(1, 10)
lst.remove(3)
lst.pop(2)
lst.index(10)
lst.count(1)
lst.reverse()
lst.sort()
```

---

## 3. 복사

### 얕은 복사

```python
a = [1, 2, 3]
b = a[:]
c = a.copy()
```

### 깊은 복사

```python
import copy
a = [[1], [2]]
b = copy.deepcopy(a)
```

---

## 4. 딕셔너리 (dict)

키는 고유하고 불변  
값은 중복 가능

- clear()
- get(key, default)
- keys()
- values()
- items()
- pop(key, default)
- setdefault(key, default)
- update(other_dict)

```python
d = {"a": 1, "b": 2}
d.get("a")
d.get("z", 0)
d.keys()
d.values()
d.items()
d.pop("a")
d.setdefault("c", 3)
d.update({"b": 4, "d": 5})
```

---

## 5. 세트 (set)

중복 없음  
순서 없음  
빠른 연산 가능

- add(x)
- clear()
- remove(x)
- discard(x)
- pop()
- update(iterable)

```python
s = {1, 2, 3}
s.add(4)
s.clear()
s = {1, 2, 3}
s.remove(2)
s.discard(5)
s.pop()
s.update([4, 5, 6])
```

### 집합 연산

```python
a = {1, 2, 3}
b = {3, 4, 5}
a - b
a & b
a | b
a <= b
a >= b
```

---

## 6. 메서드 체이닝

```python
text = "HeLLo"
text.swapcase().replace("L", "Z")
```

---

## 7. 해시 테이블

```python
hash("abc")
hash(123)
```

---

## 8. 내장 함수 구현

```python
def custom_len(items):
    count = 0
    for _ in items:
        count += 1
    return count
```

```python
def custom_max(items):
    max_value = items[0]
    for i in items[1:]:
        if i > max_value:
            max_value = i
    return max_value
```

```python
def custom_sum(items):
    total = 0
    for i in items:
        total += i
    return total
```

```python
def custom_index(items, value):
    for index, val in enumerate(items):
        if val == value:
            return index
    return -1
```

```python
def custom_reverse(items):
    new_list = []
    for i in range(len(items) - 1, -1, -1):
        new_list.append(items[i])
    return new_list
```
