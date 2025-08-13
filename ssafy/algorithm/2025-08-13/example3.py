v = list(input()) # 입력 1213242546566737


def DFS(v):
    visited = [False] * 7
    stack = []
    answer = []
    start = v[0]
    visited[int(v[0]) - 1] = True
    stack.append(v[0])
    answer.append(v[0])

    while False in visited:
        for i in range(len(v) // 2):
            if start == v[2 * i] and visited[int(v[2 * i + 1]) - 1] == False:
                start = v[2 * i + 1]
                visited[int(v[2 * i + 1]) - 1] = True
                stack.append(v[2 * i + 1])
                answer.append(v[2 * i + 1])
                continue
            elif start == v[2 * i + 1] and visited[int(v[2 * i]) - 1] == False:
                start = v[2 * i]
                visited[int(v[2 * i]) - 1] = True
                stack.append(v[2 * i])
                answer.append(v[2 * i])
                continue
        stack.pop()
        start = stack[-1]
    return answer


answer = DFS(v)

print(*answer)