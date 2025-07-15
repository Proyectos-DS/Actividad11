from typing import Any


class Stack:

    def _init__(self):
        self.stack: list[Any] = []
        self.size = 0

    def push(self, data: Any) -> None:
        self.stack.insert(0, data)
        self.size += 1

    def pop(self) -> Any:
        if self.size > 1:
            self.stack.pop(0)
            self.size -= 1

    def peek(self) -> Any:
        data = self.stack[0]
        return data

    def is_empty(self) -> bool:
        return self.size == 0
