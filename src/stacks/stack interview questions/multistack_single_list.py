#Describe how would you use a single python list to implement three stacks . Use Fixed-partitioning approach

# initialize total_size, num_stacks
# initialize stack_array of size total_size
# initialize stack_pointers array of size num_stacks, all pointing to -1

# function push(stack_num, value):
#     base_index = stack_num * (total_size // num_stacks)
#     top_index = stack_pointers[stack_num]

#     if top_index + 1 >= (total_size // num_stacks):
#         throw StackOverflow

#     stack_pointers[stack_num] += 1
#     stack_array[base_index + stack_pointers[stack_num]] = value

# function pop(stack_num):
#     base_index = stack_num * (total_size // num_stacks)
#     top_index = stack_pointers[stack_num]

#     if top_index == -1:
#         throw StackUnderflow

#     value = stack_array[base_index + top_index]
#     stack_pointers[stack_num] -= 1
#     return value

class MultiStack:
    def __init__(self, no_of_stacks, capacity_per_stack):
        self.no_of_stacks = no_of_stacks
        self.capacity_per_stack = capacity_per_stack
        self.stack_sizes = [0] * no_of_stacks
        self.storage = [0] * self.capacity_per_stack * self.no_of_stacks
        
    def is_full(self, stack_index ):
        return self.stack_sizes[stack_index ] == self.capacity_per_stack
    
    def is_empty(self, stack_index ):
        return self.stack_sizes[stack_index ] == 0
    
    def top_index(self, stack_index ):
        offset = stack_index  * self.capacity_per_stack #stack_index starts at 0 for k stacks
        return offset + self.stack_sizes[stack_index ] - 1
        
    def pop(self, stack_index ):
        if self.is_empty(stack_index):
            raise ValueError("empty stack error")
        top_index = self.top_index(stack_index)
        top_val = self.storage[top_index]
        self.storage[top_index] = 0
        self.stack_sizes[stack_index] -=1
        return top_val
    
    def push(self, stack_index , value):
        if self.is_full(stack_index):
            raise OverflowError("stack is full")
        self.stack_sizes[stack_index] += 1  
        self.storage[self.top_index(stack_index)] = value
        