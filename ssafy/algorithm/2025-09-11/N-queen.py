# def check(row, col):
#     # 1. 같은 열에 놓은 적이 있는가?
#     for i in range(row):
#         if visited[i][col]:
#             return False
        
#     # 2. 좌상단 대각선에 놓은 적이 있는가? (\)
#     i, j = row - 1, col - 1
#     while i >= 0 and j >= 0:
#         if visited[i][j]:
#             return False
#         i -= 1
#         j -= 1
        
#     # 3. 우상단 대각선에 놓은 적이 있는가? (/)
#     i, j = row - 1, col + 1
#     while i >= 0 and j < N:
#         if visited[i][j]:
#             return False
#         i -= 1
#         j += 1
        
#     return True

# # 종료 조건: N개의 행을 모두 고려하면 종료
# # 가지의 수: N개의 열
# def recur(row):
#     global answer

#     if row == N:
#         answer += 1
#         return
    
#     for col in range(N):
#         # 가지치기: 같은 열을 못 고르도록
#         # -> 유망하지 않은 케이스 모두 삭제 (세로, 대각선)
#         if check(row, col) is False:
#             continue

#         # col을 선택했다.
#         visited[row][col] = 1
#         recur(row + 1)
#         visited[row][col] = 0

# N = 15
# answer = 0  # 가능한 정답의 수
# visited = [[0] * N for _ in range(N)]
# recur(0)

# print(answer)

def check(row):
    # 1. 같은 열에 놓은 적이 있는가?
    for prev_row in range(row):
        if visited[row] == visited[prev_row]:
            return False
        
        # 2. 대각선에 놓은 적이 있는가? (\, /)
        if abs(row - prev_row) == abs(visited[row] - visited[prev_row]):
            return False
        
    return True

# 종료 조건: N개의 행을 모두 고려하면 종료
# 가지의 수: N개의 열
def recur(row):
    global answer

    if row == N:
        answer += 1
        return
    
    for col in range(N):
        visited[row] = col  # 현재 row의 col에 놓았다고 가정
        # 가지치기: 유망하지 않은 케이스 모두 삭제 (세로, 대각선)
        if check(row) is False:
            continue

        recur(row + 1)

N = 15
answer = 0  # 가능한 정답의 수
visited = [0] * N
recur(0)

print(answer)