class MyQueue(object):

    def __init__(self):
        self.object = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.object.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        ret = self.object[0]
        self.object = self.object[1:]
        return ret

    def peek(self):
        """
        :rtype: int
        """
        return self.object[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.object) == 0 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()