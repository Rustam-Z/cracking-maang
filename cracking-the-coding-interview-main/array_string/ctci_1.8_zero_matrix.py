"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

SOLUTION:
1. Iterate through the matrix and check if any element is 0. Find its row and column index, and save in lists.
2. Iterate though the columns and rows lists and set values to 0.

Time: O(rc), where r is the number of rows and c is the number of columns.
Space: O(n), number of zeros in the matrix.
"""


def zero_matrix(matrix):
    columns = set()
    rows = set()
    
    for r in range(len(matrix)):  # Row traverse
        for c in range(len(matrix[0])):  # Column traverse
            if matrix[r][c] == 0:
                columns.add(c)
                rows.add(r)
                
    # Rows change to zero
    for row in rows:
        matrix[row] = [0] * len(matrix[0])
        
    # Columns change to zero
    for column in columns:
        for row in range(len(matrix)):
            matrix[row][column] = 0
            
    return matrix


if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(zero_matrix(matrix))
