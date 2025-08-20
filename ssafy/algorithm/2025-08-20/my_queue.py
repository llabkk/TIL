# front와 rear를 사용해서 큐 만들기

# 큐의 크기
N = 3

# 공백 상태의 큐를 생성
q = [0] * N

# front : 마지막에 삭제한 원소의 위치
# rear : 마지막에 삽입한 원소의 위치
front = rear = -1

# 1, 2, 3 삽입하기
for i in range(1, N + 1):
    rear += 1 # enq(1)
    q[rear] = i

print(q)

for j in range(N):
    front += 1 # deq()
    if j != N-1:
        print(q[front], end=", ")
    else:
        print(q[front])
print(f"{q}\nfront = {front}, rear = {rear}")