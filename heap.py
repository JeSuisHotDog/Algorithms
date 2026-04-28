class Heap:
    def __init__(self):
        self.elements = []

    # Lets you run print() nicely of the heap
    def __str__(self):
        return str(self.elements)

    def size(self) -> int:
        # Return size of Heap
        return len(self.elements)

    def is_empty(self) -> bool:
        # Returns if empty or now
        return len(self.elements) == 0

    def insert(self, element: int) -> None:
        # Adds elements to Heap
        self.elements.append(element)
        i = len(self.elements) - 1
        while i > 0 and self.elements[i] > self.elements[(i - 1) // 2]:
            parent = (i - 1) // 2
            self.elements[i], self.elements[parent] = (
                self.elements[parent],
                self.elements[i],
            )
            i = parent

    def extract_max(self) -> any:
        # Removes and returns max element
        if len(self.elements) == 0:
            raise ValueError("List is empty")
        max_val = self.elements[0]
        self.elements[0] = self.elements[-1]
        self.elements.pop()
        return max_val

    def get_max(self) -> any:
        # Returns max element
        if len(self.elements) == 0:
            raise ValueError("List is empty")

        return self.elements[0]


def test_add():
    h = Heap()
    h.insert(30)
    h.insert(20)
    h.insert(40)
    h.insert(10)
    h.insert(100)
    print(h)
    print(h.extract_max())



test_add()
