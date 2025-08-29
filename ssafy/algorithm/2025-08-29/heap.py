# max_heap


def enq(n):
    global last
    last += 1  # 마지막 정점 추가
    heap[last] = n

    c = last
    p = c // 2  # 완전 이진 트리 자식 -> 부모 번호 연산

    # 부모가 있고, 부모 < 자식, 키값 교환

    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


def deq():
    global last
    root = heap[1]
    heap[1] = heap[last]
    last -= 1

    p = 1
    c = p * 2

    while c <= last:
        if c + 1 <= last and heap[c] < heap[c + 1]:
            c += 1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c *= 2
        else:
            break
    return root

    # delete = heap[1]
    # heap[1] = heap[last]
    # heap[last] = 0
    # last -= 1

    # p = 1
    # cl = 2 * p
    # cr = 2 * p + 1

    # if delete == 0:
    #     return "stop"
    # while cl <= last:
    #     if cr <= last and heap[cl] < heap[cr]:
    #         heap[p], heap[cr] = heap[cr], heap[p]
    #         p = cr
    #         cl = 2 * p
    #         cr = 2 * p + 1
    #     else:
    #         heap[p], heap[cl] = heap[cl], heap[p]
    #         p = cl
    #         cl = 2 * p
    #         cr = 2 * p + 1
    # return delete


heap = [0] * 11
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

print(heap)

while last > 0:
    print(deq())
    print(heap)
