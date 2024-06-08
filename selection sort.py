def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

numbers = list(map(int, input("Enter the list of numbers separated by space: ").split()))

print("Original list:", numbers)
selection_sort(numbers)
print("Sorted list:", numbers)