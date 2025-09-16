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

def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    # 사이클 발생
    if rep_x == rep_y:
        return
    
    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y
    return

V, E = map(int, input().split())

# 1. 간선들을 가중치 기준으로 정렬
edge = []

for _ in range(E):
    start, end, weight = map(int, input().split())
    edge.append((start, end, weight))

# 가중치 기준 오름차순 정렬
edge.sort(key=lambda x: x[2])

# 2. 가중치가 작은 간선부터 순서대로 선택
# 사이클이 발생하면 고르지 말자!
# MST가 완성될 때까지 == V-1개를 선택할 때까지

# 현재까지 선택한 간선의 수
cnt = 0

# 가중치의 합
result = 0

# make_set(V)
parents = [i for i in range(V)]

for u, v, w in edge:
    # 사이클이 아니라면
    # 연결(같은 집합으로 만든다.)
    # cnt += 1
    # cnt가 V -1이라면 종료
    if find_set(u) != find_set(v):
        union(u, v)
        cnt += 1
        result += w

        if cnt == V - 1:
            break

print(f"최소 비용 = {result}")
