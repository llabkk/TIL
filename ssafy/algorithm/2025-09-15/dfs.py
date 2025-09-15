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

def dfs(node):
    print(node, end=" ")
    
    # 다음 재귀 호출
    # node로 부터 갈 수 있는 노드들을 모두 확인
    # --> 그 중 한 곳으로 진행
    for next_node in graph[node]:
        # 이미 방문한 지점은 가지말것
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)

V, E = map(int, input().split())

# 인접 리스트 (연결된 간선만 저장) (중첩 리스트)
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    # 무향(양방향)그래프의 경우 아래 코드 추가
    graph[end].append(start)

# 방문 여부 기록
visited = [0] * (V + 1)
visited[1] = 1
dfs(1)