"""
Input: boxes = "110"
Output: [1,1,3]

Input: boxes = "001011"
Output: [11,8,5,4,3,4]

HOW:
- Create a list boxes = [0, 0, 1, 0, 1, 1]
- Loop over each element
    - if 1 then boxes[1_index] - boxes[i]
"""

class Solution:
    def minOperations(self, boxes):
        boxes = list(boxes)

        result = []

        for i in range(len(boxes)):
            sum = 0
            for j in range(len(boxes)):
                if int(boxes[j]) == 1:
                    sum += abs(j - i)
            result.append(sum)
        return result

boxes = "001011"
sol = Solution()
print(sol.minOperations(boxes))