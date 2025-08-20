N = 10

# 원형 큐 초기화
cq = [0] * N
front = rear = 0

# 원형큐는 front를 위한자리 1개를 비워둔다.

def is_full():
    return (rear + 1) % N == front

for i in range(1, 11):
    if not is_full():
        rear = (rear + 1) % N
        cq[rear] = i

print(cq)
print(f"front : {front}, rear : {rear}")

for i in range(9):
    front = (front + 1) % N
    print(cq[front], end=", ")

print()
print(cq)
# front를 위해 비워둔 자리는 삭제할때마다 바뀐다.
print(f"front : {front}, rear : {rear}")

def is_empty():
    return rear == front

# def enqueue(item):
