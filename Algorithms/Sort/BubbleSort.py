
def BubbleSort(array: list) -> list:
    """
    BubbleSort(array) --> Sorts a given List 'array'
                          by Bubble sort algorithm
                          and returns the sorted array.
    """
    for i in range(len(array)-1):
        # Run for i..len(array)-1 times
        for j in range(1, len(array)-i):
            #Swap if array[j-1] > array[j]
            if array[j-1] > array[j]:
                array[j], array[j-1] = array[j-1], array[j]
    return array


if __name__ == "__main__":

    array = [12, 3, 5, 1, 9, 5, 4]
    # print(BubbleSort.__doc__)
    print(BubbleSort(array))