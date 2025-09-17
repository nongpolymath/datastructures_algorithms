def bubble_sort(cust_list):
    total_length = len(cust_list)  
    for i in range(total_length-1): # final pass not needed hence total_length-1
        for j in range(total_length - i -1):
            # total_length - i - 1 ensures we don’t compare elements already sorted at the end of the list.
            if cust_list[j]> cust_list[j+1]:
                cust_list[j+1], cust_list[j] = cust_list[j], cust_list[j+1]     # Time complexity o(N^2)
    return cust_list

# Use bubble sort when input is already sorted, space is a concern , easy 
# avoid when time complexity is a concern
