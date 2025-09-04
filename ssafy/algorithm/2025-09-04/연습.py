# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

# for i in range(1, 4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             for m in range(1, 4):
#                 print(i, j, k, m)

# path = []
# N = 7
#
# def run(n):
#     if n == N:
#         print(path)
#         return
#     for i in range(1, N+1):
#         path.append(i)
#         run(n+1)
#         path.pop()
# run(0)

# def KFC(n):
#     if n == 10:
#         return
#     KFC(n+1)
#
# KFC(0)
# print("end")

# def print_depth(n):
#     if n == 6:
#         return
#     print(n, end=" ")
#     print_depth(n+1)
#     print(n, end=" ")
#
# print_depth(0)

# 중복 순열
# [0, 1, 2] 2개의 카드가 존재, 2개를 뽑는다.

# 기저조건(종료조건) : 2개의 카드를 모두 뽑았다면 종료
# - 시작점 : 0개의 카드를 고른 상태부터 시작
# 다음 재귀호출 구조 : [0, 1, 2] 카드 중 하나를 고른다.
# path = []
#
# def recur(n):
#     if n == 2:
#         print(*path)
#         return
#     for i in range(3):
#         path.append(i)
#         recur(n+1)
#         path.pop()
#
# recur(0)

# path = []
# # 골라야하는 수 만큼 만들어 준다.
# # used = [False] * 3
# # 1~7까지의 카드 사용 여부를 확인
# used = [False] * 7
#
# def recur(n):
#     if n == 3:
#         print(*path)
#         return
#     for i in range(1, 7):
#         # in 함수가 안의 모든 리스트를 순회하므로 느림
#         # if i in path:
#         #     continue
#         if used[i]:
#             continue
#
#         used[i] = True
#         path.append(i)
#         recur(n+1)
#         used[i] = False
#         path.pop()
#
# recur(0)

# path = []
# answer = 0
#
# def recur(n):
#     global answer
#     if sum(path) > 10:
#         return
#     if n == 3:
#         if sum(path) <= 10:
#             print(*path)
#             answer += 1
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         recur(n+1)
#         path.pop()
#
# recur(0)
#
# print(answer)

# answer = 0
#
# def recur(n, s):
#     global answer
#
#     if s > 10:
#         return
#
#     if n == 3:
#         answer += 1
#         return
#
#     for i in range(1, 7):
#         recur(n+1, s+i)
#
# recur(0, 0)
#
# print(answer)

path = []
result = 0

cards = ["A", "J", "Q", "K"]

# 연속된 3개가 나오면 return True, 아니면 False
def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False

def recur(n):
    global result

    if n == 5:
        if count_three():
            result += 1
            print(*path)
        return

    for idx in range(len(cards)):
        path.append(cards[idx])
        recur(n+1)
        path.pop()

recur(0)

print(result)