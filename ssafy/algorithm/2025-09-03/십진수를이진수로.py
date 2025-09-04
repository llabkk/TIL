decimal = 149

# 10진수를 바꾼 결과
result = []

# 2로 나눈 몫이 2보다 작아질 때까지 계속 나눈다
# 나머지를 거꾸로 읽으면 이진수 완성

while decimal != 0:
    result.append(decimal % 2)

    # 다음에 나눌 숫자
    decimal //= 2

result.reverse()

print(result)

# 비트연산자
def bit_print(dec):
    # 2진수 결과 문자열
    output = ""

    # i는 왼쪽으로 시프트한 횟수(2진수의 자리수)
    # 높은 수부터 뒤에 추가
    for i in range(7, 0, -1):
        if dec & (1 << i):
            output += "1"
        else:
            output += "0"

    # 작은 수부터 앞에 추가
    for i in range(8):
        if dec & (1 << i):
            output = "1" + output
        else:
            output = "0" + output
    
    print(output)

bit_print(149)
