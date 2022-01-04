
def InsertionSort(array: list) -> list:
    """
    InsertionSort(array) --> Sorts a given List 'array'
                             by Insertion sort algorithm
                             and returns the sorted array.
    """
    for i in range(1, len(array)):
        # Select Element
        key = array[i]

        # Insert key into sorted sequence array[1....j-1]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key

    return array


if __name__ == "__main__":

    array = [12, 3, 5, 1, 9, 5, 4]
    # print(InsertionSort.__doc__)
    print(InsertionSort(array))
