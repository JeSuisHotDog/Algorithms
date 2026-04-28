class StackArray():
	def __init__(self):
		self.elements = []

	def push(self, element: any) -> None:
		self.elements.append(element)

	def pop(self) -> any:
		if self.is_empty():
			raise ValueError("Can't pop from empty stack")
		return self.elements.pop()

	def peek(self) -> any:
		if self.is_empty():
			raise ValueError("Can't peek from empty stack")
		return self.elements[-1]

	def is_empty(self) -> bool:
		return len(self.elements) == 0

	def size(self) -> int:
		return len(self.elements)

if __name__ == "__main__":
    s = StackArray()
    s.push(1)
    s.push(5)
    s.push(3)
    print(s.pop())
    print(s.peek())
    print(s.size())
    print(s.is_empty())