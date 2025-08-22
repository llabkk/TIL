'''
전위 순회
- 전위 순회하여 정점의 번호를 출력
  - 첫 줄에는 트리의 정점의 총 수 V, 그 다음 줄에는 V-1개 간선 정보가 나열됨
  - 간선은 그것을 이루는 두 정점으로 표기
  - 간선은 항상 "부모 자식" 순서로 표기되며, 아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선으로 1이 부모 2가 자식을 의미

입력 값:
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
N = int(input())

node  = list(map(int, input().split()))

# 자식노드 번호 인덱스에 부모 번호 저장
parent = [0] * (N + 1)
# 부모번호 인덱스에 자식번호를 리스트로 묶어 저장
child = [[]for _ in range(N + 1)]

# 부모 번호를 인덱스로 왼쪽 자식 저장
left = [0] * (N + 1)

# 부모 번호를 인덱스로 오른쪽 자식 저장
right = [0] * (N + 1)

for i in range(N-1):
    parent[node[2*i+1]] = node[2*i]
    child[node[2*i]].append(node[2*i+1])
    
    # 왼쪽 자식이 비어있다면
    if left[node[2*i]] == 0:
        left[node[2*i]] = node[2*i+1]
    # 왼쪽 자식이 존재한다면
    else:
        right[node[2*i]] = node[2*i+1]

# DFS(정렬되어있으므로 전위순회로 기능)
def DFS():
    stack = []
    visited = [0] * (N + 1)
    stack.append(1)
    visited[1] = 1
    print(1, end=" ")

    while stack:
        for i in range(1, N+1):
            if parent[i] == stack[-1] and visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                print(i, end=" ")
                break
        else:
            stack.pop()
# 전위 순회
def preorder(T):
    if T:
        print(T, end= " ")
        preorder(left[T])
        preorder(right[T])

# 중위 순회
def inorder(T):
    if T:
        inorder(left[T])
        print(T, end= " ")
        inorder(right[T])

# 후위 순회
def postorder(T):
    if T:
        postorder(left[T])
        postorder(right[T])
        print(T, end= " ")

for j in range(1, N+1):
    if parent[j] == 0:
        root = j
        break

DFS()
print()

preorder(root)
print()

inorder(root)
print()

postorder(root)