### 2차원 List
#### 2차원 배열
2차원 배열의 선언
- 1차원 list를 묶어놓은 list
- 2차원 이상의 다차원 list는 차원에 따라 index를 선언
- 2차원 list의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함
```python
arr = [[0,1,2,3],[4,5,6,7]]
```

입력을 2차원 배열에 저장하기
```python
# 입력
# 3
# 1 2 3
# 4 5 6
# 7 8 9
N = int(input)
arr = [list(map(int, input().split())) for _ in range(N)]

# 입력
# 3
# 123
# 456
# 789
N = int(input)
arr = [list(map(int, input())) for _ in range(N)]

# 0으로 채워진 3x4 배열 만들기
arr = [[0] * 4 for _ in range(3)]

# N x M 배열의 크기와 저장된 값이 주어질 때
# 입력
# 3 4
# 1 7 2 8
# 6 2 9 3
# 5 7 4 2
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 합을 구하면
s = 0

for i in range(N):
    for j in range(M):
        s += arr[i][j]
```

지그재그 순회
```python
# i 행의 좌표
# j 열의 좌표
for i in range(n):
    for j in range(m):
        # 행이 홀수일때 열의 마지막인덱스(m-1)부터 시작하여 j만큼 감소
        f(array[i][j + (m-1-2*j) * (1%2)])
```

커다란 배열(NxM)에서 작은 배열(2x3)로 순회
```python
for i in range(N-1):
    for j in range(M-2):
        for a in range(i, i+2):
            for b in range(j, j+3):
                print(lst[a][b])
```

#### 델타
델타를 활용한 2차원 배열의 탐색
- 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
- 인덱스 (i,j)인 칸의 상하좌우 칸(ni, nj)

```pseudocode
di[] ← [0, 1, 0, -1] # 방향별로 더할 값
dj[] ← [1, 0, -1, 0]

for k : 0 -> 3
    ni <- i + di[k]
    nj <- j + dj[k]
```

델타를 활용한 2차원 배열 탐색
```pseudocode
arr[0...N-1][0...N-1] # NxN 배열
di[] ← [0, 1, 0, -1] # 방향별로 더할 값
dj[] ← [1, 0, -1, 0]

for i : 0 -> N-1
    for j : 0 -> N-1
        for d in range(4)
            ni <- i + di[d]
            nj <- j + dj[d]
            if 0<=ni<N and 0<=nj<N
                f(arr[ni][nj])
```
```python
dij = [[0,1], [1,0], [0,-1], [-1,0]]

for i in range(N):
    for j in range(N):
        for di, dj in dij:
            ni, nj = i+di, i+dj
            ...
```
델타응용
- NxN 배열에서 각 원소를 중심으로, 상하좌우 k칸의 합계 중 최대값(k=2)
```python
max_v = 0
for i in range(N):
    for j in range(N):
        s = arr[i][j]
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:  # 각 방향별
            for c in range(1, k+1):                 # 각 거리별
                ni, nj = i+di*c, j+dj*c
                if 0<=ni<N and 0<=nj<N:
                    s += arr[ni][nj]
        if max_v < s:
            max_v = s
```

전치행렬
```python
arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

#### 연습문제
연습문제1
- 5x5 2차원 배열에 25개의 숫자를 저장하고,
- 대각선 원소의 합을 구하시오.

연습문제2
- 5x5 2차 배열에 25개의 숫자를 저장하고,
- 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.