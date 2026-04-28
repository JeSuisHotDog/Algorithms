class IndexedList():
	class Node:
		def __init__(self, data: any = None):
			self.data = data
			self.next = None

	def __init__(self):
		self.front = None
		self.num_elements = 0

	# Lets you run a print() command on your indexedlist and get a nice output.
	def __str__(self):
		if self.front is None:
			return '[]'
		
		string = '['
		walker = self.front
		while walker != None:
			string += str(walker.data) + ', '
			walker = walker.next

		string = string[:-2]
		string += ']'
		return string

	def size(self) -> int:
		count = 0
		walker = self.front
		while walker is not None:
			count += 1
			walker = walker.next
		return count

	def is_empty(self) -> bool:
		return self.front is None

	def get_at(self, index: int) -> any:
		walker = self.front
		for i in range(index):
			if walker is None:
				return None
			walker = walker.next
		return walker.data

	def get(self, element: any) -> any:
		walker = self.front
		while walker is not None:
			if walker.data == element:
				return walker.data
			walker = walker.next
		raise ValueError('List is empty')


	def add_at(self, index: int, element: any) -> None:
		new_node = self.Node(element)
		if index == 0:
			new_node.next = self.front
			self.front = new_node
			return
		walker = self.front
		for i in range(index-1):
			walker = walker.next
		new_node.next = walker.next
		walker.next = new_node

	def remove_first(self) -> any:
		if self.front is None:
			raise ValueError('List is empty')
		data = self.front.data
		self.front = self.front.next
		return data

	def remove_at(self, index: int) -> any:
		if self.front is None:
			raise ValueError('List is empty')
		if index == 0:
			data = self.front.data
			self.front =self.front.next
			return data
		walker = self.front
		for i in range(index-1):
			walker = walker.next
		data = walker.next.data
		walker.next = walker.next.next
		return data

	def remove_last(self) -> any:
		if self.front is None:
			raise ValueError('List is empty')
		if self.front.next is None:
			data = self.front.data
			self.front = None
			return data
		walker = self.front
		while walker.next.next is not None:
			walker = walker.next
		data = walker.next.data
		walker.next = None
		return data

	def first(self) -> any:
		if self.front is None:
			raise ValueError('List is empty')
		data = self.front.data
		return data

	def last(self) -> any:
		if self.front is None:
			raise ValueError('List is empty')
		walker = self.front
		while walker.next is not None:
			walker = walker.next
		return walker.data

if __name__ == '__main__':
	ll = IndexedList()
	ll.add_at(0, 1)
	ll.add_at(1, 2)
	ll.add_at(2, 3)
	ll.add_at(1, 99)
	print(ll)