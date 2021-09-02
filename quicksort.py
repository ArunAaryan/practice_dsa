def quicksort(low, high, arr):
    if low < high:
        pivot_index = partition(low, high, arr)
        quicksort(low, pivot_index - 1, arr)
        quicksort(pivot_index + 1, high, arr)

def partition(low, high, arr):
    pivot = high
    i = low - 1
    for j in range(low, high):
        if arr[j] < arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high] , arr[i + 1]
    return i + 1

arr = [8,213,9,1,10,10,14,23,35,4,31,2]
quicksort(0, len(arr) - 1, arr)
print(arr)




