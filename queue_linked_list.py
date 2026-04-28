class QueueLinkedList():
	class Node():
		def __init__(self, data: any = None, next_node = None) -> None:
			self.data = data
			self.next = next_node

	def __init__(self) -> None:
		self.head = None
		self.tail = None
		self.num_element = 0
		
	def enqueue(self, element: any) -> None:
		new_node = self.Node(element)
		if self.tail is not None:
			self.tail.next = new_node
		self.tail = new_node
		if self.head is None:
			self.head = new_node
		self.num_element += 1

	def dequeue(self) -> any:
		if self.head is None:
			raise ValueError("Can't dequeue from empty queue")
		to_return = self.head.data
		self.head = self.head.next
		self.num_element -=  1
		return to_return

	def peek(self) -> any:
		if self.head is None:
			raise ValueError("Can't peak from empty queue")
		return self.head.data

	def is_empty(self) -> bool:
		return self.head is None

	def size(self) -> int:
		return self.num_element
