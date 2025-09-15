'''
입력1

7 8
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7

입력2

7 8
0 1 1 0 0 0 0
1 0 0 1 1 0 0
1 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0 
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
'''
from collections import deque

def bfs():
    while que:
        r = que.popleft()
        print(r, end=" ")

        for c in range(1, V + 1):
            if graph[r][c] and not visited[c]:
                visited[c] = 1
                que.append(c)

V, E = map(int, input().split())

# 인접 행렬
# 7 * 7의 배열 (1 ~ 7 정점 번호를 활용)
graph = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    graph[start][end] = 1
    # 무향(양방향)그래프의 경우 아래 코드 추가
    graph[end][start] = 1

visited = [0] * (V + 1)
visited[1] = 1

# que의 의미: 다음에 방문해야 할 노드들 (후보열, 대기열)
que = deque([1])

bfs()