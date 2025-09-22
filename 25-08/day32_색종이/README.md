# 색종이 문제 풀이 회고

## 문제 개요
주어진 색종이를 좌표 평면 위에 차례대로 붙이고, 각 색종이가 보이는 면적을 구하는 문제다.  
색종이가 겹칠 수 있기 때문에 뒤에 붙은 색종이가 앞의 색종이를 가리면 앞 색종이의 면적은 줄어들게 된다.  

## 접근 방법
1. 1000×1000 크기의 2차원 배열을 만들어 초기화했다.  
2. 색종이를 붙일 때는 해당 좌표 범위를 색종이 번호로 채우는 방식으로 구현했다.  
3. 면적 계산은 모든 좌표를 순회하면서 색종이 번호가 있으면 그 색종이의 면적 배열에 1씩 더해주는 방식으로 진행했다.  

## 개선 포인트
원래는 이중 for문을 사용해 하나씩 채웠는데, 리스트 슬라이싱을 이용하여 한 줄 단위로 값을 넣는 방식으로 바꾸었다.  
이렇게 하니 코드가 간결해지고 실행 속도도 빨라졌다.  
또한 면적 계산 시 불필요하게 count 변수를 선언했는데 단순히 area[j] += 1만으로 충분했다.  

## 배운 점
리스트에 같은 값을 여러 개 넣을 때 [값] * 개수 형태로 넣을 수 있다는 점을 배웠다.  
문제 크기가 크지 않다면 2차원 배열을 전부 쓰는 것이 오히려 단순하고 직관적인 해법이라는 점도 알게 되었다.  
겹침 여부를 따로 판별할 필요 없이 최종적으로 덮인 색종이 번호만 기록하면 된다는 것도 중요한 포인트였다.  

## 최종 코드
```python
N = int(input())
lst = [[0 for _ in range(1001)] for _ in range(1001)]

def colorpaper(width, height, x, y, count):
    global lst
    for i in range(height, height+y):
        lst[i][width:width+x] = [count]*x

for i in range(1, N+1):
    width, height, x, y = map(int, input().split())
    colorpaper(width, height, x, y, i)

area = [0]*(N+1)
for i in lst:
    for j in i:
        if j:
            area[j] += 1

for i in range(1, N+1):
    print(area[i])
