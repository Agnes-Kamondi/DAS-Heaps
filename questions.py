# 1. Implement heap sort. Given an array of integers, sort it using heap sort.

def heapify(arr, n, i):

    #Ensure the subtree rooted at index i is a heap.
    #This function assumes that the subtrees are already heaps.

    largest = i  # Initialize largest as root
    l = 2 * i + 1  # Left child
    r = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Check if right child exists and is greater than largest
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):

    #Perform heap sort on the input array.

    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move current root to end
        heapify(arr, i, 0)  # Call max heapify on the reduced heap

arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array is", arr)


# 2. Find the k-th larget element in an unsorted array
import heapq

def find_kth_largest(nums, k):
    
   # Find the k-th largest element in an unsorted array.
    
    return heapq.nlargest(k, nums)[-1]  # Find the k largest elements and return the k-th largest


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"The {k}th largest element is {find_kth_largest(nums, k)}")

# 3. Given k sorted arrays, merge then into a single sorted array 
import heapq

def merge_k_sorted_arrays(arrays):
    
    #Merge k sorted arrays into a single sorted array.
    
    min_heap = []  # Min-heap to store the smallest elements from each array
    result = []

    # Initialize heap with the first element of each array
    for i, array in enumerate(arrays):
        if array:
            heapq.heappush(min_heap, (array[0], i, 0))

    # Extract the smallest element from the heap and add the next element from the same array
    while min_heap:
        val, arr_idx, ele_idx = heapq.heappop(min_heap)
        result.append(val)
        if ele_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(min_heap, (arrays[arr_idx][ele_idx + 1], arr_idx, ele_idx + 1))

    return result

arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
print("Merged array:", merge_k_sorted_arrays(arrays))


# 4. Given an interger array return the k most frequent elements 
from collections import Counter
import heapq

def top_k_frequent(nums, k):

    #Find the k most frequent elements in an array.

    count = Counter(nums)  # Count frequency of each element
    return heapq.nlargest(k, count.keys(), key=count.get)  # Find the k most frequent elements


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(f"The {k} most frequent elements are {top_k_frequent(nums, k)}")



# 5. Given an n * n matrix where each of the rows and columns are sorted in an ascending order , find the k-th smallest element in the matrix
import heapq

def kth_smallest(matrix, k):
    
    #Find the k-th smallest element in a matrix where each row and column is sorted.
    
    n = len(matrix)
    min_heap = []  # Min-heap to store the smallest elements from the matrix

    # Initialize heap with the first element of each row
    for i in range(n):
        heapq.heappush(min_heap, (matrix[i][0], i, 0))

    # Extract the smallest element from the heap and add the next element from the same row
    while k > 0:
        val, r, c = heapq.heappop(min_heap)
        k -= 1
        if k == 0:
            return val
        if c + 1 < n:
            heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
print(f"The {k}th smallest element is {kth_smallest(matrix, k)}")

