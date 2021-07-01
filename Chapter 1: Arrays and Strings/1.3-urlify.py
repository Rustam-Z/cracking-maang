def replace_spaces(s, true_length):
    s = s[:true_length]
    return '%20'.join(s.split())

s = "Mr John Smth    "
true_length = 13
print(replace_spaces(s, true_length))

"""
def replace_spaces(s, true_length):
    space_count = 0
    for i in range(true_length):
        if s[i] == ' ':
            space_count += space_count
    # Or just we can use: space_count = s.count(' ')

    index = true_length + space_count * 2

    if true_length < len(s):
        s = s[:true_length]
    
    for i in range(10, 0, -1):
        print(i)
        # do replacement in s
    return s
"""