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
                        s += lst[ni][nj] - lst[i][j]
                    else:
                        s += lst[i][j] - lst[ni][nj]
    print(s)