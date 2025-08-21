'''
입력
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

출력
1 - 2 - 3 - 4 - 5 - 7 - 6
'''

# 시작 정점은 1
s = 1

# 입력
G = list(map(int, input().split()))

# 원형 큐 사용할 때
front = rear = 0

# 원형 큐의 길이는 front 자리 1 + 정점의 개수 7
q = [0] * (7 + 1)

# 방문 확인
visited = [False] * (7+1)

adj_lst = [[] for _ in range(7+1)]

# 그래프를 인접 리스트로 변환
for i in range(len(G)):
    if i % 2 == 0:
        if G[i+1] not in adj_lst[G[i]]:
            adj_lst[G[i]].append(G[i+1])
    # 무향성 그래프면 추가
    if i % 2 == 1:
        if G[i-1] not in adj_lst[G[i]]:
            adj_lst[G[i]].append(G[i-1])

# 인접 정점 리스트를 딕셔너리로 변환
dict_g = {}
for j in range(8):
    dict_g[j] = adj_lst[j]

# 시작 정점 큐에 추가
rear += 1
q[rear] = s
visited[s] = True
result = []

while not front == rear:
    front = (front + 1) % 8
    tmp = q[front]
    for v in adj_lst[tmp]:
        if visited[v] is False:
            rear = (rear + 1) % 8
            q[rear] = v
            visited[v] = True
    result.append(tmp)

for k in range(len(result)):
    if k != len(result) - 1:
        print(result[k], end=" - ")
    else:
        print(result[k])
