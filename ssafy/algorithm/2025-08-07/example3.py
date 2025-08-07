import sys
sys.stdin = open("연습문제3_in.txt", "r")

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    n = len(arr)

    cnt = 0

    for i in range(1<<n):
        bit = [0]*n
        for j in range(n): 
            if i & (1<<j):
                bit[j] = arr[j]
        if sum(bit) == 0:
            cnt += 1
    
    print(f"#{tc} {cnt}")