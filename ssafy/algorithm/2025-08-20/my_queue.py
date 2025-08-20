front = rear = -1
my_queue = [0] * 10

rear += 1 # enq(1)
my_queue[rear] = 1

rear += 1 # enq(2)
my_queue[rear] = 2

rear += 1 # enq(3)
my_queue[rear] = 3

front += 1 # deq()
print(my_queue[front])

front += 1 # deq()
print(my_queue[front])

front += 1 # deq()
print(my_queue[front])