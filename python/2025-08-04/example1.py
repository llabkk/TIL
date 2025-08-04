T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))

    # num.sort(), 버블 정렬
    for i in range(N-1, 0, -1):
        for j in range(i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

    print(f'#{test_case} ', num[-1] - num[0])