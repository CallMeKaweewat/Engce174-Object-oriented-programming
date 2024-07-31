#  การใช้ลิสต์เป็นสแตก (Stack) และคิว (Queue)

#  การดำเนินการกับสแตก (LIFO - Last In, First Out)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
popped_item = stack.pop()
print("Popped item from stack:", popped_item) #  แสดงผล: Popped item from stack: 3

#  การดำเนินการกับคิว (FIFO - First In, First Out)
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
dequeued_item = queue.popleft()
print("Dequeued item from queue:", dequeued_item) #  แสดงผล: Dequeued item from queue: 1
