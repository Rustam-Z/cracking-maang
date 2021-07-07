"""
Rotate Matrix

Given image represented by NxN matrix, rotate it by 90 degrees

Complexity O(n^2)

[1,2,3]
[4,5,6]
[7,8,9]

Expected:
[7,4,1]
[8,5,2]
[9,6,3]

DONE!
"""

def rotate(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)
    for layer in range(int(n/2)):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first
            top = matrix[first][i] # save top

            # left -> top
            matrix[first][i] = matrix[last-offset][first]
        
            # bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]
            
            # right -> bottom 
            matrix[last][last-offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top # saved top
    return matrix

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate(matrix))

