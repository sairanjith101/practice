from collections import deque

# Initialize deque
queue = deque([1, 2, 3])

# Enqueue: Add elements to the back of the queue
queue.append(4)  # Adds 4 to the back
print("After enqueueing 4:", queue)

queue.appendleft(6)  # Adds 6 to the front
print("After enqueueing 6 at front:", queue)

# Peek: View the front element without removing it
front_element = queue[0]  # The first element is the front in the queue
print("Peek at front element:", front_element)

# Dequeue: Remove an element from the front of the queue
queue.popleft()  # Removes 1, which is the front element
print("After dequeue:", queue)
