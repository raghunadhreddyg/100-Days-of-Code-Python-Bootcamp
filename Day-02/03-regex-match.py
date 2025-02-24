"""
This is to use match function from Regular Expression (re) package.
"""

import re

text = "The quick brown fox"
pattern = r"quick"
match = re.match(pattern, text)
if match:
    print("Match found: ", match.group())
else:
    print("Match not found.")
