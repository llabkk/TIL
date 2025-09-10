def binary_search_while(target):
    left = 0                # 검색 시작점
    right = len(arr) - 1    # 검색 끝점
    cnt = 0                 # 몇번만에 검색에 성공했는가?

    while left <= right:
        mid = (left + right) // 2
        cnt += 1

        if arr[mid] == target:
            return mid, cnt  # mid 위치에 존재한다고 return
        
        # target보다 정답이 왼쪽에 있는 경우
        if target < arr[mid]:
            right = mid - 1
         
        # target보다 정답이 오른쪽에 있는 경우
        else:
            left = mid + 1
    return -1, cnt

def binary_search_recur(left, right, target):
    mid = (left + right) // 2
    if left == right and arr[left] != target:
        return -1

    if arr[mid] == target:
        return mid
    
    if target < arr[mid]:
        return binary_search_recur(left, mid - 1, target)
    else:
        return binary_search_recur(mid + 1, right, target)

arr = [4, 2, 9, 7, 11, 23, 19]

arr.sort()  # 2 4 7 9 11 19 23

# print(f"9 = {binary_search_while(9)}번째에 위치")
# print(f"4 = {binary_search_while(4)}번째에 위치")
# print(f"20 = {binary_search_while(20)}번째에 위치")

print(f"9 = {binary_search_recur(0, len(arr) - 1, 9)}번째에 위치")
print(f"4 = {binary_search_recur(0, len(arr) - 1, 4)}번째에 위치")
print(f"20 = {binary_search_recur(0, len(arr) - 1, 20)}번째에 위치")