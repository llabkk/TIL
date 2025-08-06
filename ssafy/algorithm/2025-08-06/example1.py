import sys
sys.stdin = open("연습문제1_in.txt", "r")

T = int(input())

for tc in range(T):
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]
    delta = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
    s = lst[2][2]
    k = 2

    for di, dj in delta:
        for c in range(1, k+1):
            ni = 2 + di * c
            nj = 2 + dj * c
            if 0 <= ni < 5 and 0 <= nj < 5:
                s += lst[ni][nj]
    print(s)

# 아래는 강사님 풀이
T = int(input())

for tc in range(T):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    s = 0

    for i in range(N):
        s += matrix[i][i]
        s += matrix[i][N-1-i]
    if N % 2 == 1:
        s -= matrix[N//2][N//2]

    print(s)