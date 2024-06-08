def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
arr = input("Enter the elements of the array, separated by space: ")
arr = [int(x) for x in arr.split()]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)