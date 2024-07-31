#MAX HEAP
class MaxHeap:
    def __init__(self, elements=None):
        # Initialize the heap with the given elements, or an empty list if none provided
        self.heap = elements if elements is not None else []
        # Heapify the elements to maintain the max heap property
        self.heapify()

    def heapify(self):
        # Start from the last non-leaf node and heapify down to the root
        # Last non-leaf node index is (len(self.heap) - 2) // 2
        start_index = (len(self.heap) - 2) // 2  
        # Loop through each non-leaf node index from start_index to 0
        for index in range(start_index, -1, -1):
            self._heapify_down(index)  # Call heapify down to maintain max heap property

    def _heapify_down(self, index):
        length = len(self.heap)  # Get the current length of the heap
        while index < length:  # While the index is within the bounds of the heap
            # Calculate the left and right child indices
            left = 2 * index + 1  
            right = 2 * index + 2  
            largest = index  # Assume the current index is the largest
            
            # Check if the left child exists and is greater than the current largest
            if left < length and self.heap[left] > self.heap[largest]:
                largest = left  # Update largest if left child is greater
            
            # Check if the right child exists and is greater than the current largest
            if right < length and self.heap[right] > self.heap[largest]:
                largest = right  # Update largest if right child is greater
            
            # If the largest is not the current index, swap them
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]  # Swap
                index = largest  # Move index to the largest child's index
            else:
                break  # Stop if the heap property is satisfied

    def insert(self, val):
        # Add the new value to the end of the heap
        self.heap.append(val)  
        # Restore the heap property by bubbling up the new value
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:  # While the current index is not the root
            parent_index = (index - 1) // 2  # Calculate the parent's index
            # If the current node is greater than the parent, swap them
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]  # Swap
                index = parent_index  # Move to the parent's index
            else:
                break  # Stop if the heap property is satisfied

    def delete_max(self):
        if len(self.heap) == 0:
            return None  # Return None if the heap is empty
        # Swap the root with the last element in the heap
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        # Remove the last element (which is now the max element)
        max_val = self.heap.pop()
        # Restore the heap property by bubbling down the root
        self._heapify_down(0)
        return max_val  # Return the removed max element

    def get_max(self):
        # Return the root element (max element) or None if the heap is empty
        return self.heap[0] if self.heap else None

# Create a MaxHeap instance with initial elements
max_heap = MaxHeap([10, 20, 5, 30, 15])
print("Initial Max Heap:", max_heap.heap)  # Output: [30, 20, 5, 10, 15]

# Get the maximum element from the heap
max_element = max_heap.get_max()
print("Max Element:", max_element)  # Output: 30

# Insert a new element into the max heap
max_heap.insert(25)
print("Max Heap after inserting 25:", max_heap.heap)  # Output: [30, 20, 5, 10, 15, 25]

# Delete the maximum element from the max heap
deleted_max = max_heap.delete_max()
print("Deleted Max Element:", deleted_max)  # Output: 30
print("Max Heap after deleting max element:", max_heap.heap)  # Output: [25, 20, 5, 10, 15]

# Delete another maximum element
deleted_max = max_heap.delete_max()
print("Deleted Max Element:", deleted_max)  # Output: 25
print("Max Heap after deleting max element:", max_heap.heap)  # Output: [20, 10, 5, 15]



#MIN HEAP
class MinHeap:
    def __init__(self, elements=None):
        # Initialize the heap with the given elements, or an empty list if none provided
        self.heap = elements if elements is not None else []
        # Heapify the elements to maintain the min heap property
        self.heapify()

    def heapify(self):
        # Start from the last non-leaf node and heapify down to the root
        # Last non-leaf node index is (len(self.heap) - 2) // 2
        start_index = (len(self.heap) - 2) // 2  
        # Loop through each non-leaf node index from start_index to 0
        for index in range(start_index, -1, -1):
            self._heapify_down(index)  # Call heapify down to maintain min heap property

    def _heapify_down(self, index):
        length = len(self.heap)  # Get the current length of the heap
        while index < length:  # While the index is within the bounds of the heap
            # Calculate the left and right child indices
            left = 2 * index + 1  
            right = 2 * index + 2  
            smallest = index  # Assume the current index is the smallest
            
            # Check if the left child exists and is smaller than the current smallest
            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left  # Update smallest if left child is smaller
            
            # Check if the right child exists and is smaller than the current smallest
            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right  # Update smallest if right child is smaller
            
            # If the smallest is not the current index, swap them
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]  # Swap
                index = smallest  # Move index to the smallest child's index
            else:
                break  # Stop if the heap property is satisfied

    def insert(self, val):
        # Add the new value to the end of the heap
        self.heap.append(val)  
        # Restore the heap property by bubbling up the new value
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:  # While the current index is not the root
            parent_index = (index - 1) // 2  # Calculate the parent's index
            # If the current node is smaller than the parent, swap them
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]  # Swap
                index = parent_index  # Move to the parent's index
            else:
                break  # Stop if the heap property is satisfied

    def delete_min(self):
        if len(self.heap) == 0:
            return None  # Return None if the heap is empty
        # Swap the root with the last element in the heap
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        # Remove the last element (which is now the min element)
        min_val = self.heap.pop()
        # Restore the heap property by bubbling down the root
        self._heapify_down(0)
        return min_val  # Return the removed min element

    def get_min(self):
        # Return the root element (min element) or None if the heap is empty
        return self.heap[0] if self.heap else None

# Create a MinHeap instance with initial elements
min_heap = MinHeap([10, 20, 5, 30, 15])
print("Initial Min Heap:", min_heap.heap)  # Output: [5, 10, 20, 30, 15]

# Get the minimum element from the heap
min_element = min_heap.get_min()
print("Min Element:", min_element)  # Output: 5

# Insert a new element into the min heap
min_heap.insert(3)
print("Min Heap after inserting 3:", min_heap.heap)  # Output: [3, 5, 20, 30, 15, 10]

# Delete the minimum element from the min heap
deleted_min = min_heap.delete_min()
print("Deleted Min Element:", deleted_min)  # Output: 3
print("Min Heap after deleting min element:", min_heap.heap)  # Output: [5, 10, 20, 30, 15]

# Delete another minimum element
deleted_min = min_heap.delete_min()
print("Deleted Min Element:", deleted_min)  # Output: 5
print("Min Heap after deleting min element:", min_heap.heap)  # Output: [10, 15, 20, 30]
