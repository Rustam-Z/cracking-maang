# Bit Manipulation Problems

[Must read post](https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently)

## Need to know
1. & (and), | (or), ~ (not) and ^ (exclusive-or, xor) and shift operators a << b and a >> b
2. Don't mess `&` with `*`, `*` is used for bits multiplication while `&` is AND operator
3. Two's complement and negative numbers. 
   1. Ex.: 3 is 011. Reverse all bits, 100. Add 1, 100 + 1 = 101. Then add leading one, 1101 which is -3.
4. Shifts
   1. Arithmetic left and logical left (*2) are the same, inserting zero at the end and deleting leading bits. 
      1. 100 << 1 will be 1000. Which is multiplication of 2.
   2. Arithmetic right, copying the leading bits after shift.
   3. Logical right (/2), insert zero at the beginning. 
      1. Ex.: 100 >>> 1 will be 010 which is 2. Which is the division of 4 by 2.

```
Set union A | B
Set intersection A & B
Set subtraction A & ~B
Set negation ALL_BITS ^ A or ~A
Set bit A |= 1 << bit
Clear bit A &= ~(1 << bit)
Test bit (A & 1 << bit) != 0
Extract last bit A&-A or A&~(A-1) or x^(x&(x-1))
Remove last bit A&(A-1)
Get all 1-bits ~0
```

## Tricks
1. Get bit, check if bit at position `i` is 1 or 0, `((num & (1 << i)) != 0)`
2. Set bit, change the value of the bit position `i`, `num | (1 << i)`
3. Clear bit, `num & ~(1 << i)`
4. Update bit `(num & ~(1 << i)) | ((bitIs1 ? 1 :0) << i)`


## Problems
### Count the number of ones in the binary representation of the given number
```python
def count_one(n: int):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count
```

### Missing Number
```python
def missing_number(nums):
    ret = 0;
    for i, v in enumerate(nums):
        ret ^= i
        ret ^= v
    return ret ^ nums.size()
```

