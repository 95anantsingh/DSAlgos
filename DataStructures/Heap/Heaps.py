
# Binary Heap Implementation

class Heap(object):

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.heap = []
        self.heapSize = 0

    def parent(self, i): return i//2

    def left(self, i): return (2*i) + 1

    def right(self, i): return (2*i) + 2


class MaxHeap(Heap):

    def maxHeapify(self, i: int):
        l = self.left(i)
        r = self.right(i)

        if l < self.heapSize and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r < self.heapSize and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)

    def buildMaxHeap(self, array: list):

        if len(array) > self.maxSize:
            raise Exception("Array size is larger than Heapsize")

        self.heapSize = len(array)
        self.heap = array
        for i in range((self.heapSize//2)-1, -1, -1):
            self.maxHeapify(i)

    # def maxHeapInsert

    # def heapExtractMax

    # def heapIncreaseKey

    # def heapMaximum


# class MinHeap(Heap):

    # def minHeapify()

    # def buildMinHeap():

    # def minHeapInsert

    # def heapExtractMin

    # def heapDecreaseKey

    # def heapMinimum


if __name__ == "__main__":
    maxH = MaxHeap(15)
    array = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    maxH.buildMaxHeap(array)
    print(maxH.heap)