## Top coding interview concepts

- Heap top=O(1), insert=O(log n), remove=O(log n), heapify=O(n)
- Sliding window, two pointers
- Binary search O(log n)
- DFS & BFS
- Recursion (trees, graphs, backtracking, DP and more)
- HashMaps search=O(1), insert=O(1), remove=O(1)

# Strings

### ASCII

```
### ASCII - 26 English letters

128 chars from [0, 127], 7 bit
65 → 90, “A” → “Z”
97 → 122, “a” → “z”
ord(”a”) → 97
chr(97) → “a”
```

### Alphabet

```
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1. With capital letters [A, B, C ...]
alphabet = [chr(i) for i in range(65, 91)]

2. With lower case letters [a, b, c ...]
alphabet = [chr(i) for i in range(97, 123)]

3. Dictionary 
chars = {chr(ascii_val): ascii_val - 96 for ascii_val in range(97, 97 + 26)}
Returns: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
```

### String to integer conversion

```python
def str2int(num):
	int_ = 0
	for i in num:
		int_ = int_ * 10 + ord(i) - ord('0') # Or create a dict like "0": 0, "1":1 ....
	return int_
```

# Numbers (int, float)

### Arithmetic series sum

```
def arith_sum(n:int):
    first_term = 1
		common_diff = 1
    sum_of_terms = (n * (2 * first_term + (n - 1) * common_diff)) // 2
    return sum_of_terms
```

### Get number of "1" bits

```
>>> n = 19
>>> bin(n)
'0b10011'
>>> bin(a).count('1')
3
>>> n.bit_count()
3
>>> (-n).bit_count()
3
```

# Array

### Transpose the matrix

```python
def transpose_matrix(matrix)
	return list(zip(*matrix)
```
