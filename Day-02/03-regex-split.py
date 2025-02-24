"""
This is to split a text into strings
"""

import re

text = "apple, banana, orange, grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split Result:", split_result)
