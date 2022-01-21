
# Python has a inbuilt library for implementing Heaps, as heaps
# are generally used for Priority queues the module is named heapq

import heapq

# Implemetation of Min Heap using heapq

array = [15, 4, 3, 8, 14, 9]

heapq.heapify(array)
print("After Heapify: ", array)

# Add an element to the heap
heapq.heappush(array, 10)
print("After Push 10: ", array)

# Pop minimum element
print("Smallest: ", heapq.heappop(array))
print("After Pop: ", array)

# Push and Pop
print("Smallest: ", heapq.heappushpop(array, 7))
print("After PushPop 7: ", array)

# Push and Pop, but pop after push
print("Smallest: ", heapq.heapreplace(array, 1))
print("After Replace 1: ", array)

# Get n largest elements
print("3 Largest: ", heapq.nlargest(3, array))

# Get n smallest elements
print("3 Smallest: ", heapq.nsmallest(3, array))

# heapq.merge used to merge different type of sorted sequences into
# one sorted output

#-------------------------------------#

# Implemetation of Max Heap using heapq

array = [15, 4, 3, 8, 14, 9]

neg = lambda n : n * -1

array = [neg(el) for el in array]

heapq.heapify(array)
print("\n\nAfter Heapify: ", array)

# Add an element to the heap
heapq.heappush(array, neg(10))
print("After Push 10: ", array)

# Pop minimum element
print("Largest: ", neg(heapq.heappop(array)))
print("After Pop: ", array)

# Push and Pop
print("Largest: ", neg(heapq.heappushpop(array, neg(7))))
print("After PushPop 7: ", array)

# Push and Pop, but pop after push
print("Largest: ", neg(heapq.heapreplace(array, neg(1))))
print("After Replace 1: ", array)

# Get n largest elements
print("3 Smallest: ", [neg(el) for el in heapq.nlargest(3, array)])

# Get n smallest elements
print("3 Largest: ", [neg(el) for el in heapq.nsmallest(3, array)])
