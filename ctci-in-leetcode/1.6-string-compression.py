# class Solution:
#     def compress(self, chars) -> int:
#         compressed = []
#         count_consecutive = 0
#         for i in range(len(chars)):
#             count_consecutive += 1

#             # If next char is different than current append this char to result
#             if i + 1 >= len(chars) or chars[i] != chars[i+1]:
#                 if count_consecutive != 1:
#                     compressed.append(chars[i])
#                     compressed.extend(list(str(count_consecutive)))
#                 else:
#                     compressed.append(chars[i])                               
#                 count_consecutive = 0

#         return len(compressed)


class Solution(object):

    def compress(self, chars):

        length = len(chars)

        if length < 2:
            return length

        anchor = 0 # the start position of the contiguous group of characters we are currently reading
        write = 0

        for pos, char in enumerate(chars):
            # check if we have reached the end or a different char
            # check if we are end or the next char != the current
            if (pos + 1) == length or char != chars[pos+1]:
                chars[write] = char
                write += 1

                # check if char has been repeated
                if pos > anchor:
                    # print("HEYYY", pos, anchor)
                    # check no. of times char has been repeated
                    repeated_times = pos - anchor + 1

                    # write the number
                    for num in str(repeated_times):
                        chars[write] = num
                        write += 1

                # move the anchor to the next char in the iteration
                anchor = pos + 1

        return write

sol = Solution()
chars = ["a","a","b","b","c","c","c"]
print(sol.compress(chars))