""" defining a class for frontiers """
""" contains FIFO and FILO (stack vs queue) """

class QueueFrontier:
    def __init__(self, queue=[]):
        self.queue = queue

    def add(self, node):
        self.queue.append(node)

    def pop(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0

    def contains(self, node):
        return any([node == n for n in self.queue])

    def __repr__(self):
        return f"QueueFrontier({self.queue})"

class StackFrontier:
    def __init__(self, stack=[]):
        self.stack = stack

    def add(self, node):
        self.stack.insert(0, node)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
        
    def contains(self, node):
        return any([node == n for n in self.stack])

    def __repr__(self):
        return f"StackFrontier({self.stack})"

