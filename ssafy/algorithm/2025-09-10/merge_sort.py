# # 1. 분할
# def merge_sort(li):
#     # 분할 기저 조건
#     if len(li) == 1:
#         return li
    
#     # 절반 씩 분할하여 출력
#     mid = len(li) // 2
#     left = li[:mid]
#     right = li[mid:]

#     left_list = merge_sort(left)
#     right_list = merge_sort(right)

#     merge_list = merge(left_list, right_list)
#     return merge_list

# # 2. 정복 & 병합(정렬)
# def merge(left, right):
#     # 두 리스트를 병합한 결과 리스트
#     result = [0] * (len(left) + len(right))
#     l = r = 0   # 인덱스

#     # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
#     while l < len(left) and r < len(right):
#         if left[l] <= right[r]:
#             result[l + r] = left[l]
#             l += 1
#         else:
#             result[l + r] = right[r]
#             r += 1
    
#     while l < len(left):
#         result[l + r] = left[l]
#         l += 1
        
#     while r < len(right):
#         result[l + r] = right[r]
#         r += 1
    
#     return result

# lst = [3,5,78,54,7,56,6]

# lst = merge_sort(lst)

# print(lst)

arr = [69, 10, 30, 2, 16, 8, 31, 22]

def merge_sort(start, end):
    # 1. 종료 조건
    # 더이상 분할이 불가능 할 때 까지
    if start == end - 1:
        return start, end
    
    # 2. 재귀 호출
    # 두 부분으로 나누고 합칠때 정렬
    # 두 부분으로 나누는 기준 가운데 위치
    mid = (start + end) // 2

    # 왼쪽 범위 정렬
    left_s, left_e = merge_sort(start, mid)

    # 오른쪽 범위 정렬
    right_s, right_e = merge_sort(mid, end)

    # 정렬 및 병합
    merge(left_s, left_e, right_s, right_e)

    # 병합 후 정렬 완료
    return start, end

def merge(left_s, left_e, right_s, right_e):
    # 왼쪽 범위에서 제일 작은 원소의 인덱스
    l = left_s

    # 오른쪽 범위에서 제일 작은 원소의 인덱스
    r = right_s

    # 결과로 만들어낼 배열의 길이
    N = right_e - left_s

    result = [0] * N

    # result의 위치를 가리키는 인덱스
    idx = 0

    # 병합 및 정렬 시작
    # 왼쪽에서 가장 작은거, 오른쪽에서 가장 작은거
    # 둘중에 작은거 선택해서 result의 idx위치에 저장. idx + 1

    # 1. 비교할 왼쪽, 오른쪽이 둘다 남아있는 경우
    while l < left_e and r < right_e:
        if arr[l] < arr[r]:
            result[idx] = arr[l]
            l += 1
            idx += 1
        else:
            result[idx] = arr[r]
            r += 1
            idx += 1
    
    # 2. 왼쪽 부분이나 오른쪽 부분에만 남아있는 경우

    # 2-1. 오른쪽만 남아있는 경우
    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1
    
    # 2-2. 왼쪽만 남아있는 경우
    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1

    # 정렬이 완료된 범위 (left_s ~ right_e)를 원본에 반영
    for i in range(N):
        arr[left_s + i] = result[i]
    

N = len(arr)

merge_sort(0, N)

print(arr)
