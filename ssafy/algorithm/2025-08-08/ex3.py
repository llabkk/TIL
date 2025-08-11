import sys
sys.stdin = open("ex_in.txt", "r")

# # A와 B의 글자를 차례로 늘어놓기
# A = 'ABCD'
# B = 'EFGHIJKLMN'

# N = len(A)
# M = len(B)
# i = j = 0   # A[i], B[j]
# # ans = ''
# # while i+j < N+M:    # 복사할 문자가 남아있으면
# #     if i < N:   # A에 남은 문자가 있으면
# #         ans += A[i]
# #         i += 1
# #     if j < M:
# #         ans += B[j]
# #         j += 1
# # print(ans)
# ans = [0]*(N+M)
# while i+j < N+M:
#     if i < N:
#         ans[i+j] = A[i]
#         i += 1
#     if j < M:
#         ans[i+j] = B[j]
#         j += 1
# print(''.join(ans))

s1 = input()
s2 = input()

answer = False
for i in range(len(s2)):
    if s1 == s2[i:i+4]:
        answer = True

if answer:
    print("good")
else:
    print("bad")

T = int(input())
matrix = [input() for _ in range(T)]
goal = ["ZN", "KC"]
answer = False
for i in range(T-1):
    for j in range(T-1):
        if matrix[i][j:j+2] == goal[0]:
            if matrix[i+1][j:j+2] == goal[1]:
                answer =True
if answer:
    print("good")
else:
    print("bad")

T = int(input())

matrix = [input() for _ in range(T)]
cnt = 0
for i in range(T):
    for j in range(T):
        if matrix[i][j] == "#":
            cnt += 1
print(cnt)
def robot(i, j, T, matrix, lst):
    lst[i][j] = 1
    if i-1 >= 0 and matrix[i-1][j] == "0" and lst[i-1][j] == 0:
        robot(i-1, j, T, matrix, lst)
    if i+1 < T and matrix[i+1][j] == "0" and lst[i+1][j] == 0:
        robot(i+1, j, T, matrix, lst)
    if j-1 >= 0 and matrix[i][j-1] == "0" and lst[i][j-1] == 0:
        robot(i, j-1, T, matrix, lst)
    if j+1 < T and matrix[i][j+1] == "0" and lst[i][j+1] == 0:
        robot(i, j+1, T, matrix, lst)
    return None

T = int(input())

matrix = [input() for _ in range(T)]
lst = [[0]*T for _ in range(T)]
able = 0
start_i = 0
for i in range(T):
    for j in range(T):
        if matrix[i][j] == "#":
            start_i = i
            start_j = j
            break
    if start_i:
        break
robot(start_i, start_j, T, matrix, lst)

result = 0
for i in range(T):
    for j in range(T):
        if lst[i][j] == 1:
            result += 1

print(result)