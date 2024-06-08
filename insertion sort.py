def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

numbers = list(map(int, input("Enter the list of numbers : ").split()))

print("Original list:", numbers)
insertion_sort(numbers)
print("Sorted list:", numbers)