import re

# A string.
name = "Clyde Griffiths"

# Match with named groups.
m = re.match("(?P<first>\w+)\W+(?P<last>\w+)", name)

# Print groups using names as id.
if m:
    print(m.group("first"))
    print(m.group("last"))

'''
Pattern:         (?P<first>\w+)\W+(?P<last>\w+)

(?P<first>\w+)   First named group.
\W+              One or more non-word characters.
(?P<last>\w+)    Second named group.
'''
