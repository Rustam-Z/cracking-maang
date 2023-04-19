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

How it works?
So, we change layer by layer. For example, the below is the first layer of 3x3 matrix:
[1,2,3]
[4, ,6]
[7,8,9]

for i = 0 to n
    temp = top[i]
    top[i] = left[i]
    left[i] = bottom[i]
    bottom[i] = right[i]
    right[i] = temp

Time Complexity: O(n^2) since we must iterate through the entire matrix once.
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
            print(offset, top)
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
