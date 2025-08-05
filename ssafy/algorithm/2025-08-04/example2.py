# 상자가 놓인 가로 칸의 수 입력
N = int(input())
# 각 칸의 상자 높이 입력
height = list(map(int, input().split()))
# 현재 낙차를 계산하는 박스의 높이
box = 0
# 현재 낙차
fall = 0
# 최대 낙차
max_fall = 0
 
# 인덱스[0] 부터 반복
for i in range(N):
    # 현재 낙차를 계산하는 상자가 인덱스[i]의 상자보다 높은 경우
    if box > height[i]:
        # 현재 낙차 1증가
        fall += 1
        # 현재 낙차가 최대 낙차보다 큰 경우
        if max_fall < fall:
            max_fall = fall
    # 현재 낙차를 계산하는 상자가 인덱스[i]의 상자와 낮거나 같은 경우
    elif box <= height[i]:
        # 현재 낙차가 최대 낙차보다 큰 경우
        if max_fall < fall:
            max_fall = fall
        # 낙차 초기화
        fall = 0
        # 낙차 계산하는 박스 변경
        box = height[i]
 
# 상자가 무조건 떨어지는 높이
base = 0
# 인덱스[-1]부터 역순으로 반복
for j in range(N-1, 0, -1):
    # 박스를 만나면 반복 끝
    if height[j] != 0:
        break
    # 박스를 만나기전이면 base 1 증가
    base +=1
     
# 최대 낙차와 base의 합 출력
print(max_fall + base)