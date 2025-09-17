def insertion_sort(cust_list):
    total_length = len(cust_list)          # Step 1: Get number of elements
    for i in range(1, total_length):       # Step 2: Start from 2nd element (index 1)
        temp = cust_list[i]                # Step 3: Store the current element
        j = i - 1                          # Step 4: Compare with the previous element

        # Step 5: Shift elements to the right until correct spot is found
        while j >= 0 and temp < cust_list[j]:
            cust_list[j + 1] = cust_list[j]
            j -= 1

        # Step 6: Place 'temp' into its correct position
        cust_list[j + 1] = temp

    return cust_list                       # Step 7: Return sorted list

    
def insertion_sort(cust_list):
    total_length = len(cust_list)
    for i in range(total_length-1):
        temp = cust_list[i]
        j = i-1
        while j>=0 and temp<cust_list[j]:
            cust_list[j+1] = cust_list[j]
            j -=1
        cust_list[j+1] = temp
    return cust_list
        