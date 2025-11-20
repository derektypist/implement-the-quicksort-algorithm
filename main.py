def quick_sort(arr):
    if len(arr) == 0:
        return arr

    arr_copy = arr[:]
    pivot = arr_copy.pop()
    greater = []
    lesser = []
    for element in arr_copy:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

# Examples
print(quick_sort([20,3,14,1,5]))
print(quick_sort([83,4,24,2]))
print(quick_sort([4,42,16,23,15,8]))
print(quick_sort([87,11,23,18,18,23,11,56,87,56]))
