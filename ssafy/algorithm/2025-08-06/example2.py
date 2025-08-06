import sys
sys.stdin = open("연습문제1_in.txt", "r")


T = int(input())

for tc in range(T):
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    s = 0

    for i in range(N):
        for j in range(N):
            for di, dj in delta:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if lst[ni][nj] - lst[i][j] >= 0:
                        s += (lst[ni][nj] - lst[i][j])
                    else:
                        s += (lst[i][j] - lst[ni][nj])
    print(s)

# 아래는 강사님 풀이
T = int(input())

for tc in range(T):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    total = 0

    for i in range(N):
        for j in range(N):
            abs_sum = 0
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N:
                    sub = matrix[ni][nj] - matrix[i][j]
                    if sub < 0:
                        sub = -sub
                    abs_sum += sub
            total += abs_sum
    print(total)
