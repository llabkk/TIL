def my_push(stack, a):
    global top
    if top < len(stack) - 1:
        top += 1
        stack[top] = a
    else:
        print("overflow!")

def my_pop(stack):
    global top
    if top > -1:
        # .pop 메서드 미사용
        a = stack[top]
        # .pop 메서드 사용
        # a = stack.pop(top)
        top -= 1
        print(a)
    else:
        print("underflow!")

top = -1
stack = [0]*10

my_push(stack, "a")
my_push(stack, "b")
my_push(stack, "c")

my_pop(stack)
my_pop(stack)
my_pop(stack)
my_pop(stack)

my_push(stack, 1)
my_push(stack, 2)
my_push(stack, 3)
my_push(stack, 4)
my_push(stack, 5)
my_push(stack, 6)
my_push(stack, 7)
my_push(stack, 8)
my_push(stack, 9)
my_push(stack, 10)
my_push(stack, 11)