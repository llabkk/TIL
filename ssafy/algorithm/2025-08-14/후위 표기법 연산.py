'''
6528-*2/+
'''

postfix = "6528-*2/+"

stack = [0] * 100

top = -1

# temp = 0

answer = None

for token in postfix:
    if token not in "*/+-":
        top += 1
        stack[top] = int(token)
    else:
        # temp = stack[top]
        top -= 1
        if token == "*":
            stack[top] = stack[top] * stack[top+1]
            # temp = stack[top] * temp
            # stack[top] = temp
        elif token == "/":
            stack[top] = stack[top] / stack[top+1]
            # temp = stack[top] / temp
            # stack[top] = temp
        elif token == "+":
            stack[top] = stack[top] + stack[top+1]
            # temp = stack[top] + temp
            # stack[top] = temp
        else:
            stack[top] = stack[top] - stack[top+1]
            # temp = stack[top] - temp
            # stack[top] = temp

if top == 0:
    answer = stack[top]
    top -= 1

print(answer)