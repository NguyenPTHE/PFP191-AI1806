#insertion sort:
arr = list(map(int,input("Enter a list of number").strip().split()))

def Insertion_Sort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1, n):
        key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
Insertion_Sort(arr)
print(arr)
#binary sort:
def binary_search(arr, val, start, end):
	if start == end:
		if arr[start] > val:
			return start
		else:
			return start+1
	if start > end:
		return start

	mid = (start+end)/2
	if arr[mid] < val:
		return binary_search(arr, val, mid+1, end)
	elif arr[mid] > val:
		return binary_search(arr, val, start, mid-1)
	else:
		return mid

def insertion_sort(arr):
	for i in range(1, len(arr)):
		val = arr[i]
		j = binary_search(arr, val, 0, i-1)
		arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
	return arr

x = insertion_sort(arr)
print(x)


