import heapq

arr = [20, 15, 19, 4, 13, 11]


min_heap = []

for num in arr:
    heapq.heappush(min_heap, num)
print(min_heap)

max_heap = []
for num in arr:
    heapq.heappush(max_heap, -num)
while max_heap:
    pop_num = heapq.heappop(max_heap)
    print(-pop_num, end=" ")


arr = ['apple', 'banana', 'kiwi', 'abcd', 'abca', 'lemon', 'peach', 'grape', 'pear']

dictionary = []

for word in arr:
    heapq.heappush(dictionary, (word, len(word)))

while dictionary:
    word, length = heapq.heappop(dictionary)
    print(f"{word} 길이:{length}")