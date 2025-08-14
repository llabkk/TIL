'''
6528-*2/+
'''
def get_result(postfix):
    # 계산방법
    # 토큰을 하나씩 쭉 읽는다
    # 연산자를 만나면 제일 최근에 만난 피연산자 두개 가지고 연산
    # 스택에 피연산자 저장

    stack = []

    answer = 0

    temp1 = 0
    temp2 = 0

    for token in postfix:
        if token not in "*/+-":
            stack.append(int(token))
        else:
            if token == "*":
                temp1 = stack.pop()
                temp2 = stack.pop()
                answer = temp2 * temp1
                stack.append(answer)
            elif token == "/":
                temp1 = stack.pop()
                temp2 = stack.pop()
                answer = temp2 / temp1
                stack.append(answer)
            elif token == "+":
                temp1 = stack.pop()
                temp2 = stack.pop()
                answer = temp2 + temp1
                stack.append(answer)
            else:
                temp1 = stack.pop()
                temp2 = stack.pop()
                answer = temp2 - temp1
                stack.append(answer)
    
    answer = stack.pop()
postfix = "6528-*2/+"



# stack = [0] * 100

# top = -1

# # temp = 0

# answer = None

# for token in postfix:
#     if token not in "*/+-":
#         top += 1
#         stack[top] = int(token)
#     else:
#         # temp = stack[top]
#         top -= 1
#         if token == "*":
#             stack[top] = stack[top] * stack[top+1]
#             # temp = stack[top] * temp
#             # stack[top] = temp
#         elif token == "/":
#             stack[top] = stack[top] / stack[top+1]
#             # temp = stack[top] / temp
#             # stack[top] = temp
#         elif token == "+":
#             stack[top] = stack[top] + stack[top+1]
#             # temp = stack[top] + temp
#             # stack[top] = temp
#         else:
#             stack[top] = stack[top] - stack[top+1]
#             # temp = stack[top] - temp
#             # stack[top] = temp

# if top == 0:
#     answer = stack[top]
#     top -= 1

# print(answer)