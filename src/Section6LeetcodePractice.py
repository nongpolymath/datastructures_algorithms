from typing import List
import numpy as np
def missing_number(myList, totalCount):
    # Find the missing number in an AP. Sum of an AP , Sn = n/2[2a + (n − 1) × d] where a = first number, d = difference , n = number of terms
    # for an AP of 1, 2, 3, 4 , ........................,n-1, n
    # Sn = n/2[2*1 + (n-1)*1]
    # Sn = n(n+1)/2

    sum1=0
    total_sum = ((totalCount)*(totalCount+1))/2
    for i in myList:
        sum1 = sum1+i
    missingnumber = total_sum-sum1
    return missingnumber

# missing_number([1, 2, 3, 4, 6], 6)

def find_sum_pairs(arr,target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target:
                print(f"index found at {i} {j}")
                return i,j
            elif arr[i] == arr[j]:
                continue
            else:
                continue

def find_sum_pairs_alt(arr,target):
    sum ={}
    for ind, val in enumerate(arr):
        complement = target - val
        if complement in sum:
            print(f"index found at {ind} {val} {sum[complement]}")
            return ind,sum[complement]
        sum[val] = ind
# Explanation :
# ite1 ind = 0 val = 2 ,complement = 7 {2:0,}
# ite2 ind = 1 val = 6 ,complement = 3 {2:0,6:1}
# ite3 ind = 2 val = 3 ,complement = 6 {2:0,6:1}
arr = np.array([1,2,3,4,5,6,7,8,9])

def is_number_in_array(arr1, num):
    for i in arr1:
        if i == num:
            return True
        else:
            return False
# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.

def max_product(arr):
    # TODO
    m_val = 1
    for j in range(2):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
        m_val *= arr.pop()
    return m_val
#alternate solution
def max_product(arr):
    # Initialize two variables to store the two largest numbers
    max1, max2 = 0, 0  # O(1), constant time initialization

    # Iterate through the array
    for num in arr:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment

    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication

def sumDiagonal(a):
    # return sum of diagonal elements of a 2D matrix
    sum = 0
    for n in range(0, len(a)):
        sum = sum+a[n][n]
    return sum

# Duplicate Number
# Write a function to remove the duplicate numbers on given integer array/list.
# Example
# remove_duplicates([1, 1, 2, 2, 3, 4, 5])
# Output : [1, 2, 3, 4, 5]

def remove_duplicates(my_list):
    tmp = []
    for i in my_list:
        if i not in tmp:
            tmp.append(i)
    print(tmp)
    return tmp

# Write a function to find all pairs of an integer array whose sum is equal to a given number.
# Do not consider commutative pairs.
# Example
# Output : ['2+5', '4+3', '3+4', '-2+9']
def pair_sum(arr,sum):
    output = []
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sum:
                output.append(f'{arr[i]}+{arr[j]}')
    print(output)
    return output
# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
def contains_duplicate(nums):
    unique_vals = {}
    for i in nums:
        if i in unique_vals:
            unique_vals[i] +=1
        else:
            unique_vals[i] = 1
    for k in unique_vals:
        if unique_vals[k]>1:
            return True
        else:
            return False
# Find is a list is a permutation or not of the other
def is_permutation(list1, list2):
    if len(list1) == len(list2):
        return False
    elif list1.sort() == list2.sort():
        return True


def rotate(matrix):
    left, right = 0, len(matrix[0]) - 1
    while left < right:
        for i in range(left, right):
            top, bottom = left, right
            temp = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = temp
        left += 1
        right -= 1
    print(matrix)
    return matrix


if __name__ == "__main__":
    find_sum_pairs_alt([2,6,3,9,11], 9)

    arr = [1, 7, 3, 4, 9, 5]
    # print(max_product(arr))  # Output: 63 (9*7)
    remove_duplicates([1, 1, 2, 2, 3, 4, 5])
    pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)
    rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
