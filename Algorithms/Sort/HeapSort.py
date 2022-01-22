
# adding path of Heaps.py to the system path
import os
import sys

lib_path = os.path.abspath(os.path.join("DataStructures/Heap"))
sys.path.insert(0, lib_path)

from Heaps import MaxHeap

def HeapSort(array: list) -> list:
    '''
    HeapSort(array) -> Sorts a given List 'array'
                       by IHeap sort algorithm
                       and returns the sorted array.
    '''
    # Initialize a MaxHeap with maxlength equal to array length
    maxH = MaxHeap(len(array))

    # Build a max heap
    maxH.buildMaxHeap(array)

    # Heapsort algo
    for i in range(len(array)-1, 0, -1):
        maxH.heap[0], maxH.heap[i] = maxH.heap[i], maxH.heap[0]
        maxH.heapSize -= 1
        maxH.maxHeapify(0)

    return maxH.heap


if __name__ == "__main__":
    array = [-20, -100.3, 3.3, 14, 5, 6, 13, 6, 32, 2]
    print(HeapSort(array))
    print(help(MaxHeap))
