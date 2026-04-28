class OrderedList:
    class Node:
        def __init__(self, data: any = None):
            self.data = data
            self.next = None

    def __init__(self):
        self.front = None
        self.num_elements = 0

    # Lets you run a print() command on your orderedlist and get a nice output.
    def __str__(self):
        if self.front is None:
            return "[]"

        string = "["
        walker = self.front
        while walker != None:
            string += str(walker.data) + ", "
            walker = walker.next

        string = string[:-2]
        string += "]"
        return string

    def size(self) -> int:
        # Returns size of OrderedList
        return self.num_elements

    def is_empty(self) -> bool:
        # Returns if empty or not
        return self.front is None

    def add(self, element: any) -> None:
        # Adds element
        new_node = self.Node(element)

        if self.front is None or element < self.front.data:
            new_node.next = self.front
            self.front = new_node
            self.num_elements += 1
            return

        walker = self.front
        while walker.next is not None and walker.next.data < element:
            walker = walker.next
        new_node.next = walker.next
        walker.next = new_node
        self.num_elements += 1

    def remove(self, element: any) -> any:
        # Removes specific element
        walker = self.front
        if self.front is None:
            raise ValueError('List is empty')
        if self.front.data == element:
            self.front = self.front.next
            self.num_elements -= 1
            return element

        while walker.next is not None:
            if walker.next.data == element:
                walker.next = walker.next.next
                self.num_elements -= 1
                return element
            walker = walker.next

        raise ValueError(f'Error 404: {element} not found')

    def remove_at(self, index):
        # Removes element at specific index
        walker = self.front
        if self.front is None:
            raise ValueError('List is empty')
        if index == 0:
            self.front = self.front.next
            self.num_elements -=1
            data = walker.next.data
            walker.next= walker.next.next
            return data

        for i in range(index-1):
            walker = walker.next

        walker.next = walker.next.next
        self.num_elements -= 1
        return walker.data


    def remove_first(self) -> any:
        # Removes the first element in the OrderedList
        walker = self.front
        if self.front is None:
            raise ValueError('List is empty')
        self.front = self.front.next
        self.num_elements -= 1
        return walker.data

    def remove_last(self) -> any:
        # Removes the last element in the OrderedList
        walker = self.front
        if self.front is None:
            raise ValueError('List is empty')
        if self.front.next is None:
            self.front = None
            self.num_elements -= 1
            return walker.data
        while walker.next.next is not None:
            walker = walker.next
        data = walker.next.data
        walker.next = None
        self.num_elements -= 1
        return data

    def get(self, element: any) -> any:
        # Returns the specific element searched for
        walker = self.front
        while walker is not None:
            if walker.data == element:
                return element
            walker = walker.next
        raise ValueError('List is empty')

    def first(self) -> any:
        # Returns the first element in the OrderedList
        while self.front is not None:
            return self.front.data
        raise ValueError('List is empty')

    def last(self) -> any:
        # Returns the last element in the OrderedList
        walker = self.front
        if walker is None:
            raise ValueError('List is empty')
        while walker.next is not None:
            walker = walker.next
        return walker.data

def test_1():
    ol = OrderedList()
    ol.add(20)
    ol.add(10)
    print(ol)
    assert str(ol) == "[10, 20]"

def remove_1():
    ol = OrderedList()
    ol.add(10)
    ol.add(20)
    ol.add(30)
    ol.remove(50)
    print(ol)

def remove_first_1():
    ol = OrderedList()
    ol.add(10)
    ol.add(20)
    ol.add(30)
    ol.remove_last()
    print(ol)

def get_first():
    ol = OrderedList()
    ol.add(10)
    ol.add(20)
    ol.add(30)
    ol.get(10)
    print(ol.get(10))

def return_first():
    ol = OrderedList()
    ol.add(10)
    ol.add(20)
    ol.add(30)
    print(ol.last())

remove_1()