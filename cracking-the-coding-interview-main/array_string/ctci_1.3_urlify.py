"""
Problem: Replace all spaces between words with "%20"
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
"""


def replace_space(text: str, length: int):
    text_trimmed = text.strip()
    text_trimmed.replace(" ", "%20")
    return text_trimmed


if __name__ == "__main__":
    test_data = "Mr John Smith    "
    new_str = replace_space(test_data, len(test_data))
    print(new_str)