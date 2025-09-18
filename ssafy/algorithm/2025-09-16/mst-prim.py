'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

from heapq import heappush, heappop

# # 특정 정점 기준으로 시작
# # 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 간다.
# # 작은 노드를 먼저 꺼내기 위해 우선순위큐(heapq)를 활용
# def prim(start_node):
#     # (가중치, 노드) 형태
#     pq = [(0, start_node)]

#     # visited와 동일한 역할
#     MST = [0] * V

#     # 최소 비용
#     min_weight = 0

#     while pq:
#         # 가장 작은 가중치
#         weight, node = heappop(pq)

#         # 이미 방문한 노드라면 continue
#         if MST[node]:
#             continue

#         # node로 가는 가장 작은 노드가 확정
#         MST[node] = 1
#         # 누적 가중치
#         min_weight += weight

#         for next_node in range(V):
#             # 갈 수 없으면 continue
#             if graph[node][next_node] == 0:
#                 continue
            
#             # 이미 방문 했으면 continue
#             if MST[next_node]:
#                 continue

#             heappush(pq, (graph[node][next_node], next_node))


#     return min_weight

# V, E = map(int, input().split())

# # 인접행렬
# graph = [[0] * V for _ in range(V)]

# for _ in range(E):
#     start, end, weight = map(int, input().split())
#     graph[start][end] = weight
#     # 양방향
#     graph[end][start] = weight

# # 출발 정점과 함께 시작
# # 출발 정점을 변경해도 최소비용은 동일
# # 단, 그래프 모양은 변경 될 수 있다.
# result = prim(0)

# print(f"최소 비용 = {result}")

# 선택과제 인접리스트
def prim(start_node, start_price):
    pq = [(start_price, start_node)]

    answer = 0
    
    # node방문 확인
    mst = [0] * V

    v_cnt = 0

    while v_cnt < V and pq:
        price, node = heappop(pq)

        if mst[node]:
            continue

        mst[node] = 1
        v_cnt += 1

        answer += price

        for w, next_node in graph[node]:
            if mst[next_node]:
                continue
            heappush(pq, (w, next_node))
    
    return answer

V, E = map(int, input().split())

graph = [[] for _ in range(V)]
for _ in range(E):
    start, end, weight = map(int, input().split())

    graph[start].append((weight, end))

    # 무향(양방향)
    graph[end].append((weight, start))

result = prim(0, 0)

print(result)