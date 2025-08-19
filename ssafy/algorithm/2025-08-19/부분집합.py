lst = [1, 2, 3, 4, 5]
N = len(lst)
# 부분 집합의 합이 S이하인 부분집합만 구하시오
S = 5




# 부분집합을 만드는 재귀함수
# make_set(0) : 0번 원소를 넣을지 말지
# make_set(1) : 1번 원소를 넣을지 말지

# make_set(N-1) : N-1번 원소를 넣을지 말지
# make_set(N) : N번 원소는 없음 -> 재귀호출 중단

# idx : 내가 지금 idx번 원소를 부분집합에 넣을지 말지 선택
# selected 리스트 : 내가 지금까지 부분집합에 포함할 원소들의 상태를 나타내는 변수
# selected[x] == 1(True) : x번 원소를 부분집합에 넣기로 했다
# selected[y] == 1(False) : y번 원소를 부분집합에 넣기로 했다

def make_set(idx, selected, Sum):
    # 가지치기
    if Sum > S:
        return
    # 1. 종료 조건
    if idx == N:
        # selected 배열을 보고 내가 어떤 원소를 선택했었는지 확인
        subset = []
        for i in range(N):
            if selected[i]:
                subset.append(lst[i])
        # DFS(완전탐색을 하므로 아래 if문만을 사용하는 경우는)
        # if Sum == S:
        #     print(subset)
        print(subset)
        return
    
    # 2. 재귀 호출
    # idx번 원소를 부분집합에 넣고 idx+1번 원소를 판단하기
    selected[idx] = 1
    make_set(idx+1, selected, Sum+lst[idx])

    # idx번 원소를 부분집합에 넣지 않고 idx+1번 원소를 판단하기
    selected[idx] = 0
    make_set(idx+1, selected, Sum)


make_set(0, [0] * N, 0)