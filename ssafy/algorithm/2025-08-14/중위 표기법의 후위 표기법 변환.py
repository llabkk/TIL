'''
(6+5*(2-8)/2)
'''

stack = [0] * 100
top = -1

icp = {"(":3, "*":2, "/":2, "+":1, "-":1} # 밖에 있을때의 우선 순위(클수록 높음)
isp = {"(":0, "*":2, "/":2, "+":1, "-":1} # 스택안에서의 우선 순위(클수록 높음)

# 중위 표기법
infix = "(6+5*(2-8)/2)"

# 후위 표기법
postfix = ""

for token in infix:
    # 피연산자면 후위식에 추가
    if token not in "(+-*/)":
        postfix += token
    # 닫는 괄호면 여는 괄호가 나올 때까지 스택에서 pop
    elif token == ")":
        while top>-1 and stack[top] != "(":
            postfix += stack[top]
            top -= 1
        # 스택이 남아있다면 )버림
        if top != -1:
            top -= 1
    # 닫는 괄호를 제외한 연산자라면
    else:
        # 첫 연산자거나 스택안의 연산자보다 우선순위가 높으면
        # 스택에 연산자 push
        if top == -1 or isp[stack[top]] < icp[token]:
            top += 1
            stack[top] = token
        # 스택의 연산자보다 우선순위가 낮거나 같으면
        elif isp[stack[top]] >= icp[token]:
            while top >-1 and isp[stack[top]] >= icp[token]:
                postfix += stack[top]
                top -= 1
            # 넣을 자리 도달하면 push
            top += 1
            stack[top] = token

print(postfix)