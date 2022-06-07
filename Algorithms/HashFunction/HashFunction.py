class MyHashSet:

    def __init__(self):
        self.m = 100000
        self.set = [None]*self.m
        self.p = 17
        self.a = 3
        self.b = 4
        self.h = None
        
    def add(self, key: int) -> None:
        self.h = self.__hash(key)
        if self.set[self.h] != key:
            self.set[self.h] = key
        else:
            while self.set[self.h]!=None:
                self.h += 1
            self.set[self.h] = key
        return None

    def remove(self, key: int) -> None:
        self.h = self.__hash(key)
        while self.set[self.h]!= key:
            self.h += 1
            if self.h==self.m:
                break
        if self.h!=self.m:
            self.set[self.h] = None
        return None

    def contains(self, key: int) -> bool:
        self.h = self.__hash(key)
        contains = True
        while self.set[self.h]!= key:
            self.h += 1
            if self.h==self.m:
                contains = False
                break
        return contains

    def __hash(self, key: int) -> int:
        return ((self.a * key + self.b) % self.p) % self.m


if __name__ == "__main__":
# Your MyHashSet object will be instantiated and called as such:
    obj = MyHashSet()
    fun = ["add","add","contains","contains","add","contains","remove","contains"]
    funcall =[[1],[2],[1],[3],[2],[2],[2],[2]]
    # for i in range(8):
    #     locals()[obj.fun[i]](funcall[i])
    
    print(obj.add(1),end=" ")
    print(obj.add(2),end=" ")
    print(obj.contains(1),end=" ")
    print(obj.contains(3),end=" ")
    print(obj.add(2),end=" ")
    print(obj.contains(2),end=" ")
    print(obj.remove(2),end=" ")
    print(obj.contains(2),end=" ")

    print("\n\nF")
# Yep, I was called
#     key = 100
#     obj = MyHashSet()
#     obj.add(key)
#     # obj.remove(key)
#     # param_3 = obj.contains(key)