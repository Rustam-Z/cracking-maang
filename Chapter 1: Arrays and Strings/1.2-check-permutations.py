"""
''.join(sorted(s)) # make again string

ord('A)=65

chr(65)="A"
"""

# Solution 1
def permutation1(s, t):
    if len(s) != len(t):
        return False
    return ''.join(sorted(s)) == ''.join(sorted(t))
    

s = "abc"
t = "cba"
print(permutation1(s, t))


# Solution 2
def permutation2(s1, s2):
    if len(s1) != len(s2):  # not equal length means not permutations
        return False
    
    letters = 128 * [0]  # create counts vector

    s_array = [ord(i) for i in s1]
    for c in s_array: 
        letters[c] += 1  # count the number of each letter

    for i in s2: 
        c = ord(i)
        letters[c] -= 1
        if letters[c] < 0:
            return False
    return True
    

s = "abc"
t = "cba"
print(permutation2(s, t))