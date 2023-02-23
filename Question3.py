#Q3
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def binary_search_recursive(arr, key, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search_recursive(arr, key, left, mid-1)
    else:
        return binary_search_recursive(arr, key, mid+1, right)

def binary_search_iterative(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

num_list = []
while True:
    num = int(input("Enter an integer (1-100), or 0 to finish: "))
    if num == 0:
        break
    elif 1 <= num <= 100:
        num_list.append(num)
    else:
        print("Invalid input. Please enter an integer between 1 and 100.")

sorted_list = selection_sort(num_list)

print("Sorted list:", sorted_list)


key = int(input("Enter a key to search for using binary search (recursive): "))
result = binary_search_recursive(sorted_list, key, 0, len(sorted_list)-1)
if result == -1:
    print("Not found!")
else:
    print(f"Found key at position {result}")

key = int(input("Enter a key to search for using binary search (iterative): "))
result = binary_search_iterative(sorted_list, key)
if result == -1:
    print("Not found!")
else:
    print(f"Found key at position {result}")
