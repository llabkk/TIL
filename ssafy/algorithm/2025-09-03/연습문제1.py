bit = "00000010001101"

# 이진수를 7칸씩 쪼개서 10진수로 만들기
N = len(bit)

# 길이가 14니까
# 0번 ~ 6번 잘라서 바꾸고
# 7번 ~ 13번 잘라서 바꾸고
for i in range(0, N, 7):
    # i번 비트에서 7칸 잘라서 10진수로 만들고 출력
    ith_bin = bit[i : i + 7]

    # 십진수로 바꾸기
    decimal = 0

    for j in range(7):
        if ith_bin[6 - j] == "1":
            decimal += 2 ** (j)

    # for j in range(6, -1, -1):
    #     decimal += int(ith_bin[j]) * 2 ** (6 - j)

    if i == N - 7:
        print(decimal)
    else:
        print(decimal, end=", ")