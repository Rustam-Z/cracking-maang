alphabets = ['a', 'b', 'c', 'ch', 'dd', 'd', 'e', 'f', 'ff', 'g', 'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p',
             'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']
alpha_index = {}
for idx, val in enumerate(alphabets):
    alpha_index[val] = idx


def comp(s):
    result = []
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] + s[i + 1] in alpha_index.keys():
            result.append(alpha_index[s[i] + s[i + 1]])
            i += 2
        else:
            result.append(alpha_index[s[i]])
            i += 1
    print(result)
    return tuple(result)


strings = ['abcd', 'dd', 'dda', 'abcdd']
a = strings.sort(key=comp)  # sorted(strings, key=comp) aslo works.
print(strings)

"""
[0, 1, 2, 5]
[4]
[4, 0]
[0, 1, 2, 4]
['abcdd', 'abcd', 'dd', 'dda']

So "key" argument accepts the tuple of integers, so that it then sorts them.
"""