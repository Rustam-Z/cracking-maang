"""
char_set = {}
char_set.get(smth) # get access without error
"""

def is_unique(s):
    # We can immediately return false, because there are only 128 chars in ASCII
    if len(s) > 128:
        return False

    char_set = {}
    for i in s:
        if char_set.get(i): # Already found this char in string
            return False 
        char_set[i] = True
    return True

s = "blaqwert"
print(is_unique(s))