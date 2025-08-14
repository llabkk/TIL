'''
(6+5*(2-8)/2)
'''
# 스택 밖에 있을 때 우선순위
icp = {"+":1, "-":1,"*":2,"/":2,"(":3}

# 스택 안에 있을 때 우선순위
isp = {"+":1, "-":1,"*":2,"/":2,"(":0}

# 중위 표기식을 후위 표기식으로 바꾸기
# infix : 중위 표기식
# N : 식의 길이(토큰의 개수)
def get_postfix(infix, N):
    # 결과로 출력할 후위 표기식
    postfix = ""

    stack = []

    # 중위 표기식에서 글자(토큰) 하나씩 떼어와서 후위 표기식을 만들기
    for token in infix:
        # token이 연산자인지 피연산자인지 확인
        # token이 피연산자인 경우
        if token not in "(*/+-)":
            postfix += token
        elif stack and token == ")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            if stack:
                stack.pop()
        else:
            if not stack:
                stack.append(token)
            elif stack and icp[stack[-1]] > isp[token]:
                stack.append(token)
            elif stack and icp[stack[-1]] <= isp[token]:
                while stack and icp[stack[-1]] >= isp[token]:
                    postfix += stack.pop()
                stack.append(token)
    return postfix

infix = "(6+5*(2-8)/2)"

N = len(infix)

result = get_postfix(infix, N)

print(result)

# stack = [0] * 100
# top = -1

# icp = {"(":3, "*":2, "/":2, "+":1, "-":1} # 밖에 있을때의 우선 순위(클수록 높음)
# isp = {"(":0, "*":2, "/":2, "+":1, "-":1} # 스택안에서의 우선 순위(클수록 높음)

# # 중위 표기법
# infix = "(6+5*(2-8)/2)"

# # 후위 표기법
# postfix = ""

# for token in infix:
#     # 피연산자면 후위식에 추가
#     if token not in "(+-*/)":
#         postfix += token
#     # 닫는 괄호면 여는 괄호가 나올 때까지 스택에서 pop
#     elif token == ")":
#         while top>-1 and stack[top] != "(":
#             postfix += stack[top]
#             top -= 1
#         # 스택이 남아있다면 )버림
#         if top != -1:
#             top -= 1
#     # 닫는 괄호를 제외한 연산자라면
#     else:
#         # 첫 연산자거나 스택안의 연산자보다 우선순위가 높으면
#         # 스택에 연산자 push
#         if top == -1 or isp[stack[top]] < icp[token]:
#             top += 1
#             stack[top] = token
#         # 스택의 연산자보다 우선순위가 낮거나 같으면
#         elif isp[stack[top]] >= icp[token]:
#             while top >-1 and isp[stack[top]] >= icp[token]:
#                 postfix += stack[top]
#                 top -= 1
#             # 넣을 자리 도달하면 push
#             top += 1
#             stack[top] = token

# print(postfix)