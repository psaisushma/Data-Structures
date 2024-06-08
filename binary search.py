def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
numbers = sorted(list(map(int, input("Enter the list of numbers: ").split())))
print(numbers)  
target_number = int(input("Enter a target number: "))
index = binary_search(numbers, target_number)
if index != -1:
    print(f"Target number {target_number} found at index {index}")
else:
    print(f"Target number {target_number} not found in the list")