import numpy as np
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

def traverse_2d_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for j in range(len(arr[0])):
                print(arr[i][j])

def search_element_2d_array(arr, element):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == element:
                print(f"Element {element} found at Row index {i} column index {j}")
                count += 1
    print(f"Element {element} found {count} times")
    return

def some_fun():
    data = [[[1,2], [3,4]], [[5,6],[7,8]]]
    print(fun(data[0]))


def fun(m): # m = [[1,2], [3,4]], [[5,6],[7,8]]
    v = m[0][0] # m [0][0] = [1,2]

    for row in m:
        for element in row:
            if v < element: v = element

    return v

def some_f():
    fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
    fruit_list2 = fruit_list1
    fruit_list3 = fruit_list1[:]

    fruit_list2[0] = 'Guava'
    fruit_list3[1] = 'Kiwi'

    sum = 0
    for ls in (fruit_list1, fruit_list2, fruit_list3):
        if ls[0] == 'Guava':
            sum += 1
        if ls[1] == 'Kiwi':
            sum += 20

    print(sum)


if __name__ == "__main__":
    # traverse_2d_array(twoDArray)
    # search_element_2d_array(twoDArray, 15)
    some_f()