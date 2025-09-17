# divide and conquer using a pivot element on an array
# base case - stop when your array is divided till less than 2 elements
# recurse on divided less(left) and more(right) array of the pivot element

def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x<pivot]
        right = [x for x in arr[1:] if x>pivot]
        return quick_sort(left) + [pivot]  + quick_sort(right)  
        
print(quick_sort([4,6,19,12,7,28,0,3,9,8,1]))        
