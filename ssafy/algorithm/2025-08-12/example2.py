import sys
sys.stdin = open("input.txt", "r")

def my_push(stack, top, a):
    if top < len(stack)-1:
        top += 1
        stack[top] = a
    else:
        print("overflow!")

def my_pop(stack, top):
    if top > -1:
        a = stack[top]
        top -= 1
        return a
    else:
        print("underflow!")

def censor(string):
    length = len(string)
    top = -1
    stack = [0]*length

    reverse_string = string[::-1]

    for a in reverse_string:
        if a == ")":
            my_push(stack, top, ")")
        elif a == "(":
            if stack[top] == ")":
                my_pop(stack, top)
            else:
                print("error!")
                break

T = int(input())

for tc in range(1, 1 + T):
    string = input()
    print(string)