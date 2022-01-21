
class MergeSort:
    """
    A class to perform Merge Sort on a given Array

    Attributes
    ----------
    array : list
        array to be sorted

    Methods
    -------
    sort()
        returns the sorted array.

    Usage
    -----
    sorted_array = MergeSort(unsorted_array).sort()
    
    """
    def __init__(self, array:list):
        """
        __init__(array) -> Initializes the array for the class methods.
        """
        self.array = array

    def sort(self)->list:
        """
        sort(array) -> Calls sortRecusion method on a given List 'array'
                       by Merge sort algorithm and returns the sorted array.
        """
        return self.__sortRecursion(0,len(array))

    # Private Method
    def __sortRecursion(self, first: int, last: int) -> list:
        """
        sortRecursion(self.array, first, mid, last) -> Sorts a given List 'array'
                                                       by Merge sort algorithm
                                                       and returns the sorted array.
        """
        if first < last:
            mid = (last+first)//2
            self.__sortRecursion(first, mid)
            self.__sortRecursion(mid+1, last)
            self.__merge(first, mid, last)
            return array

    # Private Method
    def __merge(self, first: int, mid: int, last: int):
        """
        merge(self.array, first, mid, last) -> Merges a given List 'array'
                                               by Merge sort algorithm.
        """

        Left = array[first:mid+1]
        Right = array[mid+1:last+1]
        Left.append(float('inf'))
        Right.append(float('inf'))

        i = j = 0

        for k in range(first, last+1):
            if Left[i] > Right[j]:
                array[k] = Right[j]
                j += 1
            else:
                array[k] = Left[i]
                i += 1
            if Left[i] == float('inf') and Right[j] == float('inf'):
                break

if __name__ == "__main__":

    array = [12, 3, 5, 1, 9, 5, 4]    
    # print(MergeSort.sort.__doc__)
    # help(MergeSort)
    print(MergeSort(array).sort())