"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
 write a method to rotate the image by 90 degrees. can you do this in place?
"""
def set_zeroes(matrix: list[list[int]]) -> None:
    ROWS , COLS = len(matrix) , len(matrix[0])
    row_mrk = any(matrix[0][j] == 0 for j in range(COLS))
    col_mrk = any(matrix[i][0] == 0 for i in range(ROWS))

    # set the marker row columns to zero from the corresponding inner matrix cell
    for i in range(1, ROWS):
        for j in range(1, COLS):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # set the inner matrix based on row / column marker = 0
    for i in range(1, ROWS):
        for j in range(1, COLS):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    if row_mrk:
        for j in range(COLS):
            matrix[0][j] = 0
    if col_mrk:
        for i in range(ROWS):
            matrix[i][0] = 0


# test harness
if __name__ == "__main__":
    cases = [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),          # no zeroes
        ([[0, 1], [2, 3]], [[0, 0], [0, 3]]),           # zero at (0,0)
        ([[1, 2], [3, 0]], [[1, 0], [0, 0]]),           # zero in interior
    ]

    for matrix, expected in cases:
        set_zeroes(matrix)
        assert matrix == expected, f"got {matrix}, expected {expected}"

    print("all tests passed")