from stack_array import StackArray

class QueueStacks:
	def __init__(self) -> None:
		self.stack_in = StackArray()
		self.stack_out = StackArray()

	def enqueue(self, element: any) -> None:
		self.stack_in.push(element)

	def dequeue(self) -> any:
		if self.stack_out.is_empty():
			while not self.stack_in.is_empty():
				self.stack_out.push(self.stack_in.pop())
		return self.stack_out.pop()

	def peek(self) -> any:
		if self.stack_out.is_empty():
			while not self.stack_in.is_empty():
				self.stack_out.push(self.stack_in.pop())
		return self.stack_out.peek()

	def is_empty(self) -> bool:
		return self.stack_out.is_empty() and self.stack_in.is_empty()

	def size(self) -> int:
		return self.stack_in.size() + self.stack_out.size()
