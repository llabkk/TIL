# # [문제] 동전의 최소 개수
# # 규칙: 큰 동전부터 나누자
# coin_list = [100, 50, 500, 10]
# target = 1730
# result = 0

# # Greedy 문제의 단골 손님
# # 정렬 연습 : 튜프이라면, 인스턴스 리스트, 역순
# #   - 예) 길이가 우선 정렬, 같은 길이는 사전 순으로 정렬
# # list.sort() vs sorted()
# coin_list.sort(reverse=True) # 큰 동전부터 사용

# for coin in coin_list:
#     possible_cnt = target // coin
#     result += possible_cnt
#     target -= coin * possible_cnt
#     # 현재 동전으로 가능한 최대 수
#     # 정답에 더해준다.
#     # 금액을 빼준다.

# print(result)

# # [문제] 화장실 문제: 대기시간의 누적합이 최소가 되는 방법
# # 규칙: 빨리 쓰는 사람이 먼저 들어가자
# time = [15, 30, 50, 10]
# result = 0

# time.sort()

# person = len(time)

# for i in range(person):
#     result += time[i] * (person - 1 - i)

# print(result)

