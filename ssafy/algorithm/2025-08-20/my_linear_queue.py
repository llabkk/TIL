# 파이썬의 리스트 메서드를 사용해서 큐 만들기

# 큐로 사용할 빈 리스트
q = []

# 1, 2, 3 삽입하기
for i in range(1, 4):
    q.append(i)

print(q)

# 원소 삭제하기
for i in range(3):
    print(q.pop(0), end=", ")
print()

print(q)