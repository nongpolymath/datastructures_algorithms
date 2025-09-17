def selection_sort(cust_list):
    total_length = len(cust_list)
    # i marks the current position in the list that we want to fill with the smallest remaining element
    for i in range(total_length):
        # Start by assuming that the smallest element in the unsorted part is at index i
        min_index = i               
        #If it finds an element smaller than the current min_index, it updates min_index to that index.
        for j in range(i+1, total_length):
            if cust_list[min_index] > cust_list[j]:     
                min_index = j
        cust_list[i], cust_list[min_index] = cust_list[min_index], cust_list[i]
    return cust_list