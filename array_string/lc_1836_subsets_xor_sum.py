class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        combinations = self.generate_combinations(nums)
        
        sum_ = 0
        for combination in combinations:
            sum_ += self.array_xor(combination)

        return sum_

    @staticmethod
    def generate_combinations(arr):
        def backtrack(start, path):
            if path:
                result.append(path)
            for i in range(start, len(arr)):
                backtrack(i + 1, path + [arr[i]])

        result = []
        backtrack(0, [])
        return result

    @staticmethod
    def array_xor(array: list) -> int:
        if not array:
            raise Exception("Error: array cannot be empty")

        result = array[0]
        for i in range(1, len(array)):
            item = array[i]
            result ^= item

        return result 
