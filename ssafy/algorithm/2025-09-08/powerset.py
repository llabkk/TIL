# # 1. 완전탐색 부분집합 pop, append
# arr = ['O', 'X']
# name = ['MIN', 'CO', 'TIM']
# path = []

# def powerset(cnt):
#     # 기저조건(3명을 모두 고려)
#     if cnt == 3:
#         print(*path)
#         return
    
#     # 재귀호출
#     # 부분집합에 포함되지 않는 경우
#     path.append(arr[1])
#     powerset(cnt + 1)
#     path.pop()

#     # 부분집합에 포함되는 경우
#     path.append(arr[0])
#     powerset(cnt + 1)
#     path.pop()

# # 0명을 고려한 상태로 시작
# powerset(0)

# # 2. 완전탐색 부분집합 lst 매개변수
# name = ['MIN', 'CO', 'TIM']

# def powerset(cnt, subset):
#     # 기저조건(3명을 모두 고려)
#     if cnt == 3:
#         print(*subset)
#         return
    
#     # 재귀호출
#     # 부분집합에 포함시키는 경우
#     powerset(cnt + 1, subset + [name[cnt]])

#     # 부분집합에 포함 시키지 않는 경우
#     powerset(cnt + 1, subset)

# # 0명을 고려한 상태로 시작
# powerset(0, [])

# # 3. 바이너리 카운팅
# arr = [1, 2, 3, 4]

# # i: 0~2^n == i번째 부분집합
# for i in range(1 << len(arr)):
#     for idx in range(len(arr)):
#         if i & (1 << idx):
#             print(arr[idx], end=" ")
#     print()

# # 3-1. 바이너리 카운팅 

# # 검사하고자 하는 비트를 오른쪽으로 하나씩 shift 하면서 체크하는 코드
# def get_sub(tar):
#     print(f"target = {tar}", end=" / ")
#     for i in range(len(arr)):
#         # 0x1 로 표기한 이유(사실 1, 0b1, 0b0001, True 모두 가능)
#         # - 비트 연산임을 명시하는 권장방법
#         if tar & 0x1: # 가장 우측 비트를 체크
#             print(arr[i], end=" ")
#         tar >>= 1

# for target in range(1 << len(arr)):
#     get_sub(target)
#     print()