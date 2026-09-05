import heapq

# Start with a random list
data = [10, 1, 5, 2, 7]

# 1. Turn the list into a heap
heapq.heapify(data) 
print(f"Heapified list: {data}") # Output: [1, 2, 5, 10, 7] (Note: not fully sorted!)

# 2. Add a new element
heapq.heappush(data, 0)
print(f"Smallest is now: {data[0]}") # Output: 0

# 3. Pop the smallest element
smallest = heapq.heappop(data)
print(f"Popped: {smallest}") # Output: 0
print(f"New smallest: {data[0]}") # Output: 1


numbers = [10, 20, 5, 35, 15]

# Step 1: Negate all values and heapify
max_heap = [-x for x in numbers]
heapq.heapify(max_heap)

print(f"Heapified list: {max_heap}") # Output: [1, 2, 5, 10, 7] (Note: not fully sorted!)
# Step 2: Push a new value (remember to negate it!)
heapq.heappush(max_heap, -50)

# Step 3: Pop the largest value
# Pop and then multiply by -1 to get the original number back
largest = -heapq.heappop(max_heap)
print(f"The largest value is: {largest}")  # Output: 50

# Step 4: Peek at the current largest without popping
current_largest = -max_heap[0]
print(f"The current largest is: {current_largest}")  # Output: 35
