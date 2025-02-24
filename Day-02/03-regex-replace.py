"""
This is to replace a string in text using re package

"""

import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"
replacement = "red"
new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)
