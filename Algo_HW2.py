"""1. Split in Half
Given a string. Split it into two equal parts. Swap these parts and return the result.
If the string has odd characters, the first part should be one character greater than the second part.
Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

2. Unique Characters in String
Given a string, determine if it consists of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False.
Hint: https://www.w3schools.com/python/python_sets.asp"""


def split_in_half(s: str):
    return s[len(s) // 2 + 1:] + s[:len(s) // 2 + 1] if len(s) % 2 != 0 else s[len(s) // 2:] + s[:len(s) // 2]


def unique_characters_in_string(s: str):
    for elem in s:
        if s.count(elem) > 1:
            return False
    return True


print(split_in_half('bbbbbcaaaaa'))
print(unique_characters_in_string('aabcde'))