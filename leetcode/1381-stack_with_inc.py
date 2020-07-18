class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if self.maxSize == len(self.stack): return
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack: return -1
        popped = self.stack[-1]
        self.stack = self.stack[:-1]
        return popped

    def increment(self, k: int, val: int) -> None:
        i = min(k, len(self.stack))
        self.stack[:i] = [x + val for x in self.stack[:i]]

