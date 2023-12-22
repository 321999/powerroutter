'''
Implement stack using queue without using an array or linked list.
○ Push
○ Pop
○ Top
Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
Front: Get the front item from queue – Time Complexity : O(1)
Rear: Get the last item from queue – Time Complexity : O(1)
'''
# as we know queue is open at both side jo pahile aayega vo pahile jayega 
# from ast import Return
# queue=[1,2,3,4,4,5]
 
# # def top():
# #     Return queue[-1]

# print(queue.pop()) 
# from queue import Queue 
# # setting the size of queue to 5
# q=Queue(maxsize=5) 
# # now queue is empty  [a,2,3,4]
# print(q.empty()) 
# q.put("a")   
# q.put(2)   
# q.put(3)   
# print(q)  
# q.put(4)   
# print(q.qsize())  
# print(q.get())
# print(q)  


'''
To implement stack using queue which is FIFO 
in simple word we have to convert the FIFO to LIFO
AS WE KNOW IN QUEUE, element entered from back that is rear and remove from frontend 
'''
from collections import deque
# we have to import the double ended queue which means queue should be behave like a stack
# and for that element should be entered and remove from same end 
# to do this we have to import double ended queue 

class StackUsingQueue:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    # 
    def push(self, value):
        # Add the element to queue1
        self.queue1.append(value)

    def pop(self):
        if not self.queue1:
            return None  # Stack is empty

        # Move elements from queue1 to queue2 except the last element
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        # Pop the last element from queue1 (this is equivalent to popping from the stack)
        popped_value = self.queue1.popleft()

        # Swap the names of queue1 and queue2, so queue1 remains the primary queue
        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_value

    def top(self):
        if not self.queue1:
            return None  # Stack is empty

        # Move elements from queue1 to queue2 except the last element
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        # Get the last element from queue1 (this is equivalent to getting the top of the stack)
        top_value = self.queue1[0]

        # Move the last element back to queue1
        self.queue2.append(self.queue1.popleft())

        # Swap the names of queue1 and queue2, so queue1 remains the primary queue
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_value

# Example usage:
stack = StackUsingQueue()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.top())  # Output: 3
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1
print(stack.pop())  # Output: None (stack is empty)

