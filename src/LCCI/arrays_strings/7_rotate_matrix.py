'''
Chapter 01 - Problem 07 - Rotate Matrix - CTCI 6th Edition page 91

Problem Statement:
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?

Example:
[1,2,3,       [7,4,1,
 4,5,6,   ->   8,5,2,
 7,8,9]        9,6,3]
'''
from typing import List

def rotate(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix) , len(matrix[0])
        for i in range(ROWS):
            for j in range(COLS):
                if j>i:
                    matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        
        for i in range(ROWS):
            left , right = 0 , COLS - 1
            while left < right:
                matrix[i][left] , matrix[i][right] = matrix[i][right] , matrix[i][left]
                left +=1
                right -=1


if __name__ == "__main__":
    test_cases = [
        (
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            [[7, 4, 1],
             [8, 5, 2],
             [9, 6, 3]]
        ),
        (
            [[5, 1, 9, 11],
             [2, 4, 8, 10],
             [13, 3, 6, 7],
             [15, 14, 12, 16]],
            [[15, 13, 2, 5],
             [14, 3, 4, 1],
             [12, 6, 8, 9],
             [16, 7, 10, 11]]
        ),
        (
            [[1]],
            [[1]]
        ),
        (
            [[1, 2],
             [3, 4]],
            [[3, 1],
             [4, 2]]
        ),
    ]

    passed = 0
    for idx, (matrix, expected) in enumerate(test_cases):
        rotate(matrix)  # mutates in place
        status = "PASS" if matrix == expected else "FAIL"
        if status == "PASS":
            passed += 1
        print(f"Test {idx + 1}: {status}")
        print(f"  got:      {matrix}")
        print(f"  expected: {expected}")

    print(f"\n{passed}/{len(test_cases)} tests passed")