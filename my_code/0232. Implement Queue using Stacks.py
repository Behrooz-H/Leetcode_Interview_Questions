"""
232- Implement a queue using a stack
Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

"""


class MyQueue:

    def __init__(self):
        self.q, self.aux=[],[]
    def push(self, x: int) -> None:
        self.q.append(x)
        return
    def pop(self) -> int:
        res =self.q[-1]
        self.q=self.q[:-1]
        return res
    def peek(self) -> int:
        return self.q[-1]
    def empty(self) -> bool:
        self.q=[]
        return True

if __name__=="__main__":
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(x=2)
    obj.push(x=3)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
