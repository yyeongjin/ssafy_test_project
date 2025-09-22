## 박스타입 (Box Type)

박스 타입에 따라 페이지에서의 배치 흐름과 다른 박스와의 관계가 달라진다.

### 1. Block 타입

- 항상 **새로운 행**에서 시작한다.
- `width`, `height`, `margin`, `padding` 속성 모두 적용 가능.
- `margin`, `padding`, `border`로 인해 다른 요소들을 밀어낸다.
- 대표적인 태그: `div`, `h1~h6`, `p`, `section`, `article`, `header`, `footer` 등.

### 2. Inline 타입

- 단어에 **형광펜 칠하는 것**과 유사하다.
- 줄바꿈이 발생하지 않는다.
- `width`, `height` 속성을 직접 지정할 수 없다.
- 대표적인 태그: `a`, `img`, `span`, `strong`, `em` 등.
- `span`: 자체적으로 시각적 변화는 없으나, **텍스트 일부를 조작**할 때 활용.

```css
.index {
  display: inline;
}

```

### 3. Inline-block 타입

- `inline`과 `block`의 특성을 모두 가진다.
- 줄바꿈 없이 **크기 지정 가능**.
- 예시:

```css
.menu {
  display: inline-block;
  width: 100px;
  height: 50px;
}

```

### 4. None 타입

- 요소를 **화면에 표시하지 않음**.
- 공간조차 차지하지 않는다.
- `visibility: hidden`은 공간은 차지하지만 보이지 않음.

---

## Normal Flow

- 일반적인 흐름에서 요소가 배치되는 방식.
- 별도의 레이아웃 속성을 지정하지 않은 기본 상태.

---

## CSS Layout

웹 페이지의 요소를 배치하는 방법.

- **display**: `block`, `inline`, `flex`, `grid`
- **position**: `static`, `relative`, `absolute`, `fixed`, `sticky`

---

## CSS Position

### Position 속성 유형

1. **static**
    - 기본값.
    - `top`, `right`, `bottom`, `left` 속성이 적용되지 않음.
2. **relative**
    - Normal flow를 유지하면서, 자신을 기준으로 상대적 이동.
3. **absolute**
    - Normal flow에서 제거.
    - 가장 가까운 **position 속성이 있는 조상**을 기준으로 배치.
4. **fixed**
    - Normal flow에서 제거.
    - *뷰포트(브라우저 화면)**를 기준으로 고정.
5. **sticky**
    - `relative`와 `fixed`의 특성을 결합.
    - 스크롤 위치에 따라 상대적 → 고정으로 바뀐다.

### Position 이동 방향

- `top`, `right`, `bottom`, `left` 속성으로 위치 이동 가능.

### z-index

- 요소의 **쌓임 순서**를 정의.
- 정수값을 사용하며, 값이 클수록 위로 올라옴.
- **static이 아닌 요소**에만 적용 가능.

---

## CSS Flexbox

요소를 행과 열 상태로 배치하는 **1차원 레이아웃 방식**.

### Flexbox 구성 요소

- **Flex Container**: flex 환경을 지정한 부모 요소.
- **Flex Item**: container 안에 들어간 자식 요소들.
- **Main axis**: 주 축 (기본은 가로).
- **Cross axis**: 교차 축 (기본은 세로).

### Flexbox 주요 속성

1. **flex-direction**
    - 아이템이 배치되는 방향 지정.
    - 값: `row`(기본), `row-reverse`, `column`, `column-reverse`.
2. **flex-wrap**
    - 아이템이 한 줄에 다 들어가지 않으면 줄바꿈 여부 결정.
    - 값: `nowrap`(기본), `wrap`, `wrap-reverse`.
3. **justify-content** (메인 축 정렬)
    - 아이템들을 주 축 기준으로 정렬.
    - 값: `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly`.
4. **align-items** (교차 축 정렬)
    - 한 줄 내에서 아이템들을 교차 축 기준으로 정렬.
    - 값: `stretch`(기본), `flex-start`, `flex-end`, `center`, `baseline`.
5. **align-content** (여러 줄 정렬)
    - 여러 줄이 있을 때 교차 축 방향으로 줄 간격을 조정.
    - 값: `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `stretch`.

---

## Flexbox 추가 속성

### 1. align-self

- **개별 flex 아이템**에 대해 교차 축 정렬을 지정.
- `align-items`가 컨테이너 전체 아이템에 적용되는 반면,`align-self`는 특정 아이템 하나만 별도로 정렬할 때 사용한다.
- 값:
    - `auto` (기본값 → 부모의 `align-items` 상속)
    - `flex-start`
    - `flex-end`
    - `center`
    - `baseline`
    - `stretch`

```css
.item1 {
  align-self: flex-start;
}
.item2 {
  align-self: center;
}
.item3 {
  align-self: stretch;
}

```

---

### 2. order

- Flex 아이템의 **배치 순서**를 변경한다.
- 기본값은 `0`, 값이 작을수록 앞쪽, 클수록 뒤쪽에 배치된다.

```css
.item1 { order: 2; }
.item2 { order: 1; }  /* item2가 더 앞에 배치됨 */
.item3 { order: 3; }

```

---

### 3. flex-grow

- 남은 **여유 공간을 차지하는 비율**을 설정.
- 기본값은 `0` (남는 공간을 차지하지 않음).
- 값이 클수록 남는 공간을 더 많이 차지한다.

```css
.item1 { flex-grow: 1; }
.item2 { flex-grow: 2; } /* item2가 item1보다 2배 넓게 늘어남 */

```

---

### 4. flex-shrink

- 공간이 부족할 때 **아이템이 줄어드는 비율**을 설정.
- 기본값은 `1` (줄어들 수 있음).
- `0`으로 설정하면 아이템이 줄어들지 않는다.

```css
.item1 { flex-shrink: 0; } /* 줄어들지 않음 */
.item2 { flex-shrink: 2; } /* 다른 아이템보다 2배 더 줄어듦 */

```

---

### 5. flex-basis

- 아이템의 **기본 크기**를 설정.
- `width`와 비슷하지만, Flexbox 문맥에서 사용된다.
- `auto`(기본값)는 콘텐츠 크기나 width 값에 따라 결정된다.

```css
.item1 { flex-basis: 200px; }

```

---

### 6. flex (단축 속성)

- `flex-grow`, `flex-shrink`, `flex-basis`를 한 번에 지정.
- 형식: `flex: grow shrink basis;`

```css
.item1 { flex: 1 1 100px; } /* grow=1, shrink=1, basis=100px */
.item2 { flex: 2; } /* grow=2, shrink=1, basis=0 */

```

---

### 7. gap (flexbox 간격)

- flex 아이템 사이의 **간격**을 지정.
- `row-gap`, `column-gap`도 가능하다.

```css
.container {
  display: flex;
  gap: 20px;
}

```

---

# Flexbox 핵심 정리

- `align-items`: 전체 아이템 교차축 정렬
- `align-self`: 개별 아이템 교차축 정렬
- `order`: 순서 변경
- `flex-grow`: 늘어나는 비율
- `flex-shrink`: 줄어드는 비율
- `flex-basis`: 기본 크기
- `flex`: grow/shrink/basis 단축
- `gap`: 아이템 간격

margin collapsing (마진 상쇄)
