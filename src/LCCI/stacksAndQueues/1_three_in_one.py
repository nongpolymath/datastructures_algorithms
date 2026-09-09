"""
1. Three in One: Describe how you could use a single array to implement three stacks.
Interview Question 03.01.

Three in one. Describe how to implement three stacks using only one array.
"""

class TripleInOne:

    def __init__(self, stackSize: int):
        self.stackSize = stackSize
        self.array = [0] * (stackSize * 3)
        self.tops = [(i * stackSize) - 1 for i in range(3)]

    def push(self, stackNum: int, value: int) -> None:
        max_index = (stackNum + 1) * self.stackSize - 1
        if self.tops[stackNum] >= max_index:
            return
        self.tops[stackNum] += 1
        self.array[self.tops[stackNum]] = value

    def pop(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        val = self.array[self.tops[stackNum]]
        self.tops[stackNum] -= 1
        return val

    def peek(self, stackNum: int) -> int:
        return self.array[self.tops[stackNum]]

    def isEmpty(self, stackNum: int) -> bool:
        return self.tops[stackNum] == stackNum * self.stackSize - 1