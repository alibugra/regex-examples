import re

# Input.
value = "abc 123 def 456 dot map pat"

# Find all words starting with d or p.
list = re.findall("[dp]\w+", value)

# Print result.
print(list)

'''
Pattern: [dp]\w+

[dp]     A lowercase d, or a lowercase p.
\w+      One or more word characters.
'''
