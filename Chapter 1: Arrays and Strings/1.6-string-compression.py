"""
String Compression

aabcccccaaa --> a2b1c5a3
If the compressed string would not become smaller than the original string, 
we method should return original string.

LEARNED:
How to solve --> "IndexError: string index out of range"

Solution #1 Time Complexity:
- O(p+k^2) where p is the size of string, k is the number of character sequences.
- k^2 because string concatenation operates in O(n^2)
    - "compressed_string += string[i] + str(count_consecutive)" this creates a new copy of a string over time
    - But if we use .append() to string somehow, copies will not be copied !???
    - https://waymoot.org/home//python_string/

"""

# Solution #1
def compress_bad(string):
    compressed_string = ""
    count_consecutive = 0
    for i in range(len(string)):
        count_consecutive += 1

        # If next char is different than current append this char to result
        if i + 1 >= len(string) or string[i] != string[i+1]:
            compressed_string += string[i] + str(count_consecutive)
            count_consecutive = 0

    # if len(compressed_string) < len(string):
    #     return compressed_string
    # else: 
    #     return string
    return compressed_string if len(compressed_string) < len(string) else string

string = "aabcccccaaa"
print(compress_bad(string))

