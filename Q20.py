# Q20. Implement a queue using collections.deque with enqueue, dequeue, and peek operations.
# Queue-> First In First Out. insert from rear delete from front

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()   #queue = deque([])  , queue is just a var name(it can be any)
    
    def enqueue(self,value):
        self.queue.append(value)  #insert at last

    def dequeue(self):
        if not self.queue:          
            return "Queue is empty"
        return self.queue.popleft()   #remove from front
    
    def peek(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue[0]          # View front element
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(10)

print("removed:",q.dequeue())
print(q.peek())


#The core implementation
from collections import deque

queue = deque()

queue.append(10)     # enqueue
queue.popleft()      # dequeue
queue[0]             # peek
# The class Queue version simply wraps these three deque operations into proper queue methods.