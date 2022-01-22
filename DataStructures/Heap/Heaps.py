
# Binary Heap Implementation

class Heap:

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

    def heapMaximum(self) -> float:
        """
        heapMaximum(self) -> Returns the maximum element.
        """
        return self.heap[0]

    def heapExtractMax(self) -> float:
        '''
        heapExtractMax(self) -> Extracts maximum element from the heap.
        '''
        if self.heapSize<0:
            raise Exception("Heap Underflow")
        max = self.heap[0]
        self.heap[0] = self.heap[self.heapSize-1]
        self.heapSize -= 1
        self.maxHeapify(0)

        # Delete last element from memory
        self.heap.pop(self.heapSize)

        return max

    def heapIncreaseKey(self, index : int, key: float):
        '''
        heapIncreaseKey(self, index, key) -> Increases the key value at given index
        '''
        try:
            if key < self.heap[index]:
                raise Exception("New key is smaller than current key")
        except IndexError:
            raise Exception("Invalid index, Heap size is: "+str(self.heapSize))

        self.heap[index] = key
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[index], self.heap[self.parent(index)] = \
            self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def maxHeapInsert(self, key:float):
        '''
        maxHeapInsert(self, key) -> Inserts the key value in the Heap.
        '''
        self.heapSize += 1
        self.heap[self.heapSize-1] = float('-inf')
        self.heapIncreaseKey(self.heapSize-1,key)


# class MinHeap(Heap):

    # def minHeapify()

    # def buildMinHeap():

    # def heapExtractMin

    # def heapMinimum

    # def heapDecreaseKey

    # def minHeapInsert


if __name__ == "__main__":
    maxH = MaxHeap(15)
    array = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    maxH.buildMaxHeap(array)
    print(maxH.heap)
    print(maxH.heapExtractMax())
    print(maxH.heap)
    
    maxH.heapIncreaseKey(0,0.1)
    print(maxH.heap)