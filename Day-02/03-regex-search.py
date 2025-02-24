"""
This is to search for a string in text using re package

"""
import re

text = " The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)

if search:
    print("The search found:", search.groups())
else:
    print("The search not found.")
