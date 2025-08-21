from collections import deque

mai = deque()
num = 1
snack = 100
v = 0

while snack > 0:
    if mai:
        temp = mai.popleft()
        snack -= temp[1]
        temp[1] += 1
        mai.append(temp)
    mai.append([num, 1])
    num += 1

print(f"마지막 받은 사람 : {temp[0]}")