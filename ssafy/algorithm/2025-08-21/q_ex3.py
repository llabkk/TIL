'''
입력
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

출력
1 - 2 - 3 - 4 - 5 - 7 - 6
'''
def bfs(s, V):
    # 초기화
    visited = [0] * (V + 1) # visited 생성
    q = [s]                 # 큐 생성

    visited[s] = 1          # 시작점 인큐 표시
    # 반복
    while q:                # 탐색할 정점이 남아 있으면
        t = q.pop(0)        # 디큐
        print(t)            # visit(), 방문 정점 출력
        for w in adj_lst[t]:    # 인접하고 미방문인 정점 인큐, 인큐 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
    return

# 입력
V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_lst = [[] for _ in range(7+1)]

# 그래프를 인접 리스트로 변환
for i in range(E):
    v1, v2 = arr[2*i], arr[2*i+1]
    adj_lst[v1].append(v2)
    # 무향성 그래프면 아래도 실행
    adj_lst[v2].append(v1)

bfs(1, V)