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