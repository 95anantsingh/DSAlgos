
import random

class QuickSort:
    def __init__(self, array: list) -> None:
        self.array = array
        self.arrsize = len(self.array)

    def sort(self, partitionType="lomuto") -> list:
        return self.__sortRecursion(0, self.arrsize-1, partitionType)

    def __sortRecursion(self, first: int, last: int, pType: str) -> list:
        if first < last:
            if pType == "lomuto":
                mid = self.__lomutoPartition(first, last)
            elif pType == "hoare":
                mid = self.__hoarePartition(first, last)
            elif pType == "random":
                mid = self.__randomizedPartition(first, last)
            self.__sortRecursion(first, mid-1, pType)
            self.__sortRecursion(mid+1, last, pType)
        return self.array

    def __lomutoPartition(self, first: int, last: int) -> int:
        # choose last element as pivot point
        pivot = self.array[last]
        i = first - 1
        for j in range(first, last):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = \
                    self.array[j], self.array[i]

        self.array[i + 1], self.array[last] = \
            self.array[last], self.array[i + 1]

        return i + 1

    def __hoarePartition(self, first: int, last: int) -> int:
        # choose first element as pivot point
        pivot = self.array[first]
        i = first
        j = last
        while True:
            while self.array[j] > pivot:
                j -= 1
            while self.array[i] < pivot:
                i += 1

            if i < j:
                self.array[i], self.array[j] = \
                    self.array[j], self.array[i]
            else:
                return j

    def __randomizedPartition(self, first: int, last: int) -> int:
        pivot = random.randint(first, last)
        self.array[pivot], self.array[last] = \
            self.array[last], self.array[pivot]
        return self.__lomutoPartition(first,last)


if __name__ == "__main__":

    array = [120, -33.3, 50, 1, 9, 5, 4]
    # print(QuickSort.sort.__doc__)
    # help(QuickSort)
    print(QuickSort(array).sort(partitionType="hoare"))
