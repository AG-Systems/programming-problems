class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = []
        self.container = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.que.append(x)
        self.container.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.container[::-1]
        val = self.container.pop()
        self.container[::-1]
        self.que = self.container
        return val

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        self.container[::-1]
        val = self.container[len(self.container)-1]
        self.container[::-1]
        return val

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.que) > 0:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
