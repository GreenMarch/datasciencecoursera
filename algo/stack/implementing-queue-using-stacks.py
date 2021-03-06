class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack2)!=0:
            return self.stack2.pop()
        else:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2)!=0:
            return self.stack2[-1]
        else:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack1)==0 and len(self.stack2)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


"""
232. Implement Queue using Stacks
Easy

720

122

Favorite

Share
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Accepted
Runtime: 40 ms
Your input
["MyQueue","push","push","peek","pop","empty"]
[[],[1],[2],[],[],[]]
Output
[null,null,null,1,1,false]
Expected
[null,null,null,1,1,false]

Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

Solution
Queue is FIFO (first in - first out) data structure, in which the elements are inserted from one side - rear and removed from the other - front. The most intuitive way to implement it is with linked lists, but this article will introduce another approach using stacks. Stack is LIFO (last in - first out) data structure, in which elements are added and removed from the same end, called top. To satisfy FIFO property of a queue we need to keep two stacks. They serve to reverse arrival order of the elements and one of them store the queue elements in their final order.

Approach #1 (Two Stacks) Push - O(n)O(n) per operation, Pop - O(1)O(1) per operation.
Algorithm

Push

A queue is FIFO (first-in-first-out) but a stack is LIFO (last-in-first-out). This means the newest element must be pushed to the bottom of the stack. To do so we first transfer all s1 elements to auxiliary stack s2. Then the newly arrived element is pushed on top of s2 and all its elements are popped and pushed to s1.


"""
