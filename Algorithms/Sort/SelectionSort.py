
def SelectionSort(array: list) -> list:
    """
    SelectionSort(array) --> Sorts a given List 'array'
                          by Selection sort algorithm
                          and returns the sorted array.
    """
    for i in range(len(array)):
        minIndex = i
        # Search of Minimum Element
        for j in range(i,len(array)):
            if array[minIndex] > array[j]:
                minIndex = j
        # Swap minimum with i'th element
        array[i],array[minIndex] = array[minIndex], array[i]
                
    return array


if __name__ == "__main__":

    array = [12, 3, 5, 1, 9, 5, 4]
    # print(SelectionSort.__doc__)
    print(SelectionSort(array))
