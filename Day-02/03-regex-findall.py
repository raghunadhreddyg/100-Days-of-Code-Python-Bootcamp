"""
 A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).

1. Regular Expressions for Text Processing:

Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
The re module in Python is used for working with regular expressions.
Common metacharacters: . (any character), * (zero or more), + (one or more), ? (zero or one), [] (character class), | (OR), ^ (start of a line), $ (end of a line), etc.
Examples of regex usage: matching emails, phone numbers, or extracting data from text.
re module functions include re.match(), re.search(), re.findall(), and re.sub() for pattern matching and replacement.
"""

import re

text = "The quick brown fox"
pattern = r"brown"
search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found.")

