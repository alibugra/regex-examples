import re

# Input string.
value = "one 1 two 2 three 3"

# Separate on one or more non-digit characters.
result = re.split("\D+", value)

# Print results.
for element in result:
    print(element)

'''
Pattern: \D+

\D+      One or more non-digit characters.
'''
