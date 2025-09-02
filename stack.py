# 堆结构，常数时间，必须得牺牲空间来处理寻找最小的元素；

# 堆的基本操作，插入，删除，更新
import math
class MinStack:
    def __init__(self):
        self.stack = []
        # 这个最小的目的是，有pop过程，需要实时保存当前zhang
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
