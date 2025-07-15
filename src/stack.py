from typing import Any

class Stack:
    
    def __init__(self):
        self.stack: list[Any] = []
        self.size = 0

    def push(self, data: Any) -> None:
        self.stack.insert(0, data)
        self.size += 1

    def pop(self) -> Any:
        if self.size > 0:
            self.size -= 1
            return self.stack.pop(0)
            

    def peek(self) -> Any:
        return self.stack[0]

    def is_empty(self) -> bool:
        return self.size == 0
