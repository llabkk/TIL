'''
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
'''

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

N = len(arr)

cnt = 0

def powerset(lst, i, s):
    global cnt
    cnt += 1
    if s > 10:
        return
    if s == 10:
        print(lst)
        return
    if i < N:
        lst.append(arr[i])
        powerset(lst, i+1, s+arr[i])
        lst.pop()
        powerset(lst, i+1, s)

powerset([], 0, 0)
print(cnt)

cnt = 0

for i in range(1 << N):
    lst = []
    s = 0
    for idx in range(N):
        cnt += 1
        if i & (1 << idx):
            lst.append(arr[idx])
            s += arr[idx]
            if s > 10:
                break
    if s == 10:
        print(lst)

print(cnt)