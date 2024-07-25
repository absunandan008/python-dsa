class MinHeap:

    def __init__(self):
        self.heap = []
        self.length = 0

    def insert(self, value):
        self.heap.append(value)
        self.shift_up(self.length)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        output = self.heap[0]
        self.length -= 1
        if self.length == 0:
            self.heap = []
            self.length = 0
            return output
        self.heap[0] = self.heap[self.length]
        self.shift_down(0)


        return

    def parent(self, index):
        return index // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def shift_up(self, index):
        if index == 0:
            return
        parent_index = self.parent(index)

        if self.heap[parent_index] > self.heap[index]:
            self.swap(index, parent_index)
            self.shift_up(parent_index)

    def shift_down(self, index):

        leftChildIndex = self.left_child(index)
        rightChildIndex = self.left_child(index)

        if index >= self.length or leftChildIndex >= self.length:
            return

        if self.heap[leftChildIndex] > self.heap[rightChildIndex] and self.heap[index] > self.heap[rightChildIndex]:
            self.swap(index, rightChildIndex)
            self.shift_down(rightChildIndex)
        elif self.heap[rightChildIndex] > self.heap[leftChildIndex] and self.heap[index] > self.heap[leftChildIndex]:
            self.swap(index, leftChildIndex)
            self.shift_down(leftChildIndex)

if __name__ == '__main__':
    heap = MinHeap()
    heap.insert(3)
    heap.insert(2)
    heap.insert(4)
    heap.insert(8)
    heap.insert(6)
    heap.insert(7)

    print(heap.heap)
    print(heap.pop())
    print(heap.length)
    print(heap.pop())
    print(heap.length)
    print(heap.pop())
    print(heap.length)
