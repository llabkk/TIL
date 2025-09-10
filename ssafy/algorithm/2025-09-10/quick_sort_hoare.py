lst = [3, 2, 4, 6, 9, 1, 8, 7, 5]

# 왼쪽 끝/ 오른쪽 끝 / 가운데 세 값 중에 중간 값을 선택

n = len(lst)

# 왼쪽 끝
def hoare_partition1(left, right):
    pivot = lst[left]
    i = left + 1      # 큰 값
    j = right         # 작은 값

    while i <= j:   # 교차되면 끝
        while i <= j and lst[i] <= pivot:
            i += 1

        while i <= j and lst[j] >= pivot:
            j -= 1

        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    
    lst[left], lst[j] = lst[j], lst[left]
    return j

# 오른쪽 끝
def hoare_partition2(left, right):
    pivot = lst[right]
    i = left      # 큰 값
    j = right - 1         # 작은 값

    while i <= j:   # 교차되면 끝
        while i <= j and lst[i] <= pivot:
            i += 1

        while i <= j and lst[j] >= pivot:
            j -= 1

        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    
    lst[right], lst[i] = lst[i], lst[right]
    return i

# 가운데
def hoare_partition3(left, right):
    mid = (left + right) // 2
    pivot = lst[mid]

    lst[left], lst[mid] = lst[mid], lst[left]

    i = left + 1      # 큰 값
    j = right         # 작은 값

    while i <= j:   # 교차되면 끝
        while i <= j and lst[i] <= pivot:
            i += 1

        while i <= j and lst[j] >= pivot:
            j -= 1

        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    
    lst[left], lst[j] = lst[j], lst[left]
    return j

def quick_sort(left, right):
    if left < right:
        pivot = hoare_partition1(left, right)
        # pivot = hoare_partition2(left, right)
        # pivot = hoare_partition3(left, right)

        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)

quick_sort(0, len(lst) - 1)
print(lst)