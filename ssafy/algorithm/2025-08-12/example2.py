def my_push(stack, a):
    global top
    if top < len(stack)-1:
        top += 1
        stack[top] = a
    else:
        print("overflow!")

def my_pop(stack):
    global top
    if top > -1:
        a = stack[top]
        top -= 1
        return a
    else:
        print("underflow!")

def censor(string):
    global top
    length = len(string)
    stack = [0]*length

    reverse_string = string[::-1]

    for a in reverse_string:
        if a == ")":
            my_push(stack, ")")
        elif a == "(":
            if stack[top] == ")":
                my_pop(stack)
            else:
                return False
    if top == -1:
        return True
    else:
        return False

T = int(input())

for tc in range(1, 1 + T):
    top = -1
    string = input()

    result = censor(string)

    if result:
        print(f"#{tc} good!")
    else:
        print(f"#{tc} error")