def quicksort(low, high, arr):
    if low < high:
        pivot_index = partition(low, high, arr)
        quicksort(low, pivot_index - 1, arr)
        quicksort(pivot_index + 1, high, arr)

def partition(low, high, arr):
    pivot = arr[high]
    pos = low  
    for small in range(low, high):
        if arr[small] < pivot:
            arr[pos], arr[small] = arr[small], arr[pos]
            pos += 1
    arr[pos], arr[high] = arr[high], arr[pos]
    return pos 


# arr = [8,213,9,1,10,10,14,23,35,4,31,2] 
import random
# arr = [2, 5, 1, 3, 9, 8]
arr = []
for _ in range(100):
    arr.append(random.randint(1, 100))
print(arr)
arr_cp = sorted(arr) 
quicksort(0, len(arr) - 1, arr)
print(arr)
print(arr == arr_cp)




