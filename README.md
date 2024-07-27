# DAS-Heaps
Heaps Data Structure 
Heaps
A heap is a specialized tree-based data structure that satisfies the heap property. In a max heap, for any given node, the value of the node is greater than or equal to the values of its children. In a min heap, the value of the node is less than or equal to the values of its children. This structure is fundamental in computer science, particularly in the implementation of priority queues.

Properties of Heaps
Complete Binary Tree: Heaps are typically implemented as complete binary trees, meaning all levels are fully filled except possibly for the last level, which is filled from left to right.
Heap Property: For max heaps, each parent node is greater than or equal to its children. For min heaps, each parent node is less than or equal to its children.
Time Complexity:
Insertion: O(log n) – When a new element is added, it is initially placed at the end of the heap. To maintain the heap property, it may need to be "bubbled up" to its correct position, which in the worst case involves traversing the height of the tree. Since a heap is a complete binary tree, the height is log(n).
Deletion: O(log n) – Deleting the root element (which is the maximum in a max heap or the minimum in a min heap) requires replacing it with the last element and then "bubbling down" to restore the heap property. This operation also involves traversing the height of the tree, which is log(n).
Peek: O(1) – Accessing the root element (the maximum in a max heap or the minimum in a min heap) is a constant time operation since it is always at the beginning of the array.
Heapify: O(n) – Transforming an arbitrary array into a heap involves building the heap from the bottom up. The heapify operation applied to each element takes logarithmic time relative to the height of the heap, but since we are doing this for all elements, the overall complexity is linear, O(n).
Space Efficiency: Heaps can be efficiently implemented using arrays, which minimizes the memory overhead and makes access patterns simple and cache-friendly.
Indexing in Heaps
Heaps are often implemented using arrays due to their space efficiency. The elements of the heap are stored in a contiguous block of memory, with the following indexing relationships:

Parent Node: For a node at index i, its parent is at index (i - 1) // 2.
Left Child: For a node at index i, its left child is at index 2i + 1.
Right Child: For a node at index i, its right child is at index 2i + 2.
This array-based representation ensures efficient use of space and simplifies the implementation of heap operations.

Applications of Heaps
Priority Queues: Heaps are used to implement priority queues where the highest (or lowest) priority element is accessed first.
Heap Sort: A comparison-based sorting algorithm that uses the heap data structure.
Graph Algorithms: Heaps are used in algorithms like Dijkstra's and Prim's for efficient minimum spanning tree and shortest path finding.
Median Maintenance: Heaps can be used to maintain the median of a dynamic dataset.
Scheduling: Heaps help in scheduling tasks in operating systems and other applications.

Advantages of Heaps
Efficient Operations: Heaps provide efficient insert and extract operations with O(log n) time complexity.
Memory Utilization: As a complete binary tree, heaps use memory efficiently.
Implementation Simplicity: Heaps can be implemented using arrays, which simplifies memory management and access patterns.

Disadvantages of Heaps
Non-Sequential Access: Heaps do not support sequential access or traversal.
Balancing Overhead: Although heaps are complete binary trees, maintaining the heap property requires overhead for balancing after insertions and deletions.

Accessing Heaps
Insertion
Adding a new element while maintaining the heap property. Typically involves placing the new element at the end and then "bubbling up" to restore the heap property.
Deletion
Removing the root element (highest priority in a max heap or lowest in a min heap) and then "bubbling down" to restore the heap property.
Peek
Accessing the root element without removing it.
Heapify
Transforming a binary tree or an array into a heap. This can be done in two ways:
Bottom-up Approach: Starting from the lowest level non-leaf nodes and moving upwards, restoring the heap property at each node.
Top-down Approach: Inserting elements one by one into an initially empty heap and restoring the heap property each time.

Other Operations
Merge: Combining two heaps into one while maintaining the heap property. This operation is complex and may vary in efficiency based on the specific heap implementation.
Increase/Decrease Key: Adjusting the value of a key and restoring the heap property. This operation is useful in priority queues where priorities may change dynamically.
Build Heap: Constructing a heap from an arbitrary array using the heapify process. This is an efficient way to initialize a heap from a given dataset.
Extract Min/Max: Removing and returning the minimum element from a min heap or the maximum element from a max heap. This is similar to the delete operation but specifically targets the root element.
Operations: Min Heap vs. Max Heap
Insertion: The process is similar for both, where the new element is added at the end and then "bubbled up." In a min heap, the element "bubbles up" if it is smaller than its parent. In a max heap, it "bubbles up" if it is larger.
Deletion: The root element is removed, and the last element is moved to the root and then "bubbled down." In a min heap, it "bubbles down" if it is larger than its children. In a max heap, it "bubbles down" if it is smaller.
Peek: In both, peeking the root element is an O(1) operation, returning the smallest element in a min heap and the largest in a max heap.

Creating a Heap
Inserting Elements: One by one into an initially empty heap.
Heapify Operation: Building a heap from an unsorted array using the heapify algorithm.

Deleting a Heap
Clear Elements: Recursively delete all elements or clear the array representing the heap.
Free Memory: Ensure that memory occupied by the elements is freed if using dynamic memory allocation.
Additional Considerations
Balancing: Heaps are naturally balanced as complete binary trees but require rebalancing after insertions and deletions to maintain the heap property.
Visualization: Use libraries or tools to visualize heaps for better understanding.
Time and Space Complexity: Analyze the time and space efficiency of different heap operations, typically O(log n) for insertion and deletion.

Why Are Heaps Used in Algorithms?
Priority Queues: Heaps allow for efficient implementation of priority queues, where elements are inserted and the highest (or lowest) priority element can be quickly accessed and removed.
Heap Sort: This sorting algorithm utilizes the heap property to sort elements in O(n log n) time, making it a useful comparison-based sorting method.
Graph Algorithms: Algorithms like Dijkstra's and Prim's rely on heaps to efficiently find the shortest path and minimum spanning tree, respectively. The ability to quickly extract the minimum (or maximum) element is crucial in these algorithms.
Dynamic Median Maintenance: Heaps can be used to maintain the median of a dynamically changing dataset, where one heap keeps track of the lower half of the data and another heap keeps track of the upper half.
Task Scheduling: Heaps are used in operating systems and other applications to schedule tasks based on priority, ensuring that the highest priority task is always executed first.
