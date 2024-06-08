def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
numbers = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)
target_number = int(input("Enter the target number: "))
index = linear_search(numbers, target_number)
if index != -1:
    print(f"Target number {target_number} found at index {index}")
else:
    print(f"Target number {target_number} not found in the list")