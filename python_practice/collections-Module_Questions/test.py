from collections import deque

num = [1,2,3]

queue = deque(num)

queue.append(4)
print(queue)

queue.appendleft(5)
print(queue)

first_ele = queue[0]
print(first_ele)

queue.pop()
print(queue)

queue.popleft()
print(queue)