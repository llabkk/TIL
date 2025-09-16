'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

from heapq import heappush, heappop

# 무한대를 가정(문제의 최대)
# 손으로 다 더했을 때 최대값이 몇일까?
INF = float("inf")

def dijkstra(start_node):
    # 누적거리, 노드번호
    pq = [(0, start_node)]

    # 각 정점까지의 최단거리를 저장할 리스트
    dists = [INF] * V

    # 시작노드 최단거리는 0
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)

        # 이미 더 작은 값으로 온 적이 있으면 버린다.
        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            # 다음 노드로 가기 위한 누적 거리
            # 누적 거리 = 현재까지의 거리 + 다음 거리
            new_dist = dist + next_dist

            # limit 가 있는 경우 가지치기
            # if limit를 넘으면:
            #     continue

            # 이미 작거나 같은 가중치로 온 적이 있다면 continue
            if dists[next_node] <= new_dist:
                continue
                
            # 누적거리, 새로운 노드를 pq에 저장 + dists에 갱신
            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return dists

V, E = map(int, input().split())

# 시작점
start_node = 0

# 인접 리스트로 구현
graph = [[] for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    # [주의] 단방향
    graph[start].append((weight, end))

# 출발지로부터 모든 최단거리
result = dijkstra(0)

print(result)

# # 선택 과제 인접 행렬로 구현
# def dijkstra(start_node):
#     pq = [(0, start_node)]

#     dists = [float("inf")] * V

#     dists[start_node] = 0

#     while pq:
#         dist, node = heappop(pq)

#         if dists[node] < dist:
#             continue

#         for i in range(V):
#             if not graph[node][i]:
#                 continue

#             if graph[node][i] + dist > dists[i]:
#                 continue
            
#             dists[i] = graph[node][i] + dist
#             heappush(pq, (graph[node][i] + dist, i))

#     return dists

# V, E = map(int, input().split())

# graph = [[0] * V for _ in range(V)]

# for _ in range(E):
#     start, end, weight = map(int, input().split())

#     graph[start][end] = weight


# result = dijkstra(0)

# print(result)

