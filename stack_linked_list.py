class StackLinkedList():
	class Node():
		def __init__(self, data: any = None, next_node = None) -> None:
			self.data = data
			self.next = next_node

	def __init__(self) -> None:
		self.top = None
		self.num_elements = 0

	def push(self, data: any) -> None:
		self.top = self.Node(data, self.top)
		self.num_elements += 1

	def pop(self) -> any:
		if self.top is None:
			raise ValueError("Can't call pop on empty stack")

		to_return = self.top.data
		to_delete = self.top
		self.top = self.top.next
		del to_delete
		self.num_elements -= 1
		return to_return

	def peek(self) -> any:
		if self.top is None:
			raise ValueError("Can't call peek on empty stack")
		return self.top.data

	def is_empty(self) -> bool:
		return self.top is None

	def size(self) -> int:
		return self.num_elements