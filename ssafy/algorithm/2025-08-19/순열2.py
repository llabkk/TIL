lst = [1,2,3]
N = 3

# 자리를 교환하는 방식
# 0 번 인덱스와 누가 자리를 바꿀래?
# 1 번 인덱스와 누가 자리를 바꿀래?
# ...
# N-1 번 인덱스와 누가 자리를 바꿀래?
# N 번 인덱스와 누가 자리를 바꿀래? => 재귀 종료

# idx : idx번에 있는 원소를 다른 위치와 자리를 교환
def make_perm(idx):
    global cnt
    # 1. 종료 조건
    if idx == N:
        print(lst)
        return
    
    # 2. 재귀 호출
    # idx번이랑 누구랑 자리바꿀래? 정해야한다.
    # N개중에 하나 고르면 된다.
    # idx번호와 비교해서 idx이상인 번호와 자리를 교환
    # 자리바꾸는 대상 j는 idx보다 앞에 있으면 안된다 => 앞에서 바꿨던 자리를 원상복구하는 경우가 생기기 때문에
    for j in range(idx, N):
        # idx와 j번 자리를 바꾼다
        lst[idx], lst[j] = lst[j], lst[idx]
        # idx+1 를 누구랑 바꿀건지 정하기
        make_perm(idx+1)
        # idx와 j번이 자리를 바꿨던 일을 없던일로 원상 복구
        lst[idx], lst[j] = lst[j], lst[idx]
make_perm(0)