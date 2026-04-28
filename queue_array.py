class QueueArray:
	def __init__(self) -> None:
		self.capacity = 100
		self.elements = [None] * self.capacity
		self.num_elements = 0
		self.head = 0
		self.tail = 0

	def _expand(self) -> None:
		new_capacity = self.capacity * 2
		new_element= [None] * new_capacity * 2
		for i in range(self.num_elements):
			new_element[i] = self.elements[(self.head + i) % self.capacity]
		self.elements = new_element
		self.head = 0
		self.tail = self.num_elements
		self.capacity = new_capacity

	def enqueue(self, element: any) -> None:
		if self.num_elements == self.capacity:
			self._expand()
		self.elements[self.tail] = element
		self.tail = (self.tail + 1) % self.capacity
		self.num_elements += 1

	def dequeue(self) -> any:
		if self.is_empty():
			raise ValueError('Queue is empty')
		to_return = self.elements[self.head]
		self.head = (self.head + 1) % self.capacity
		self.num_elements -= 1
		return to_return

	def peek(self) -> any:
		if self.is_empty():
			raise ValueError("Can't peak from empty list")
		return self.elements[self.head]

	def is_empty(self) -> bool:
		return self.num_elements == 0

	def size(self) -> int:
		return self.num_elements
