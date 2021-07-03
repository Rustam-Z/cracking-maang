"""
Palindrome = same backwards and forwards

To be a permutation of a palindrome, a string can have NO MORE THAN one character that is odd.
For both even and odd cases.

Solution #1:
- Use map to count how many times each character appears
- Then iterate to ensure NO MORE than one char has an odd count
"""

def is_permutation_of_palindrome(phrase):
    phrase = phrase.lower().replace(" ", "")
    table = build_char_frequency(phrase)
    return check_max_one_odd(table)

def check_max_one_odd(table):
    found_odd = False # We need just one odd 
    for count in table.values():
        if count % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True

def build_char_frequency(phrase):
    table = {}
    for i in phrase:
        if table.get(i): # Already found this char in string
            table[i] += 1
        else:
            table[i] = 1
        
    return table

phrase = "Tact Coa" # 2T, 2A, 2C, O
print(is_permutation_of_palindrome(phrase))