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

# V, E = map(int, input().split())

# # 인접 행렬
# # 7 * 7의 배열 (1 ~ 7 정점 번호를 활용)
# graph = [[0] * (V + 1) for _ in range(V + 1)]

# for _ in range(E):
#     start, end = map(int, input().split())
#     graph[start][end] = 1
#     # 무향(양방향)그래프의 경우 아래 코드 추가
#     graph[end][start] = 1

# for row in graph[1:]:
#     print(row[1:])



# # 인접 리스트 (연결된 간선만 저장) (중첩 리스트)
# graph = [[] for _ in range(V + 1)]

# for _ in range(E):
#     start, end = map(int, input().split())
#     graph[start].append(end)
#     # 무향(양방향)그래프의 경우 아래 코드 추가
#     graph[end].append(start)

# for row in graph[1:]:
#     print(row)

# 인접 리스트 (연결 리스트)
class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class Graph:
    def __init__(self, size):
        self.adj = [None] * (size + 1)
    
    def insert(self, u, v):
        node = Node(v)
        node.next = self.adj[u]
        self.adj[u] = node

g = Graph(5)     # 정점 5개짜리 그래프

g.insert(1, 2)   # 1 → 2
g.insert(1, 3)   # 1 → 3
g.insert(2, 4)   # 2 → 4
g.insert(3, 5)   # 3 → 5

# 인접 리스트 출력
for i in range(1, 6):
    print(i, end=": ")
    node = g.adj[i]
    while node:
        print(node.value, end=" → ")
        node = node.next
    print("None")