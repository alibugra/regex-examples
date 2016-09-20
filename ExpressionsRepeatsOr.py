import re

values = ["cat100", "---200", "xxxyyy", "jjj", "box4000", "tent500"]
for v in values:

    # Require 3 letters OR 3 dashes.
    # ... Also require 3 digits.
    m = re.match("(?:(?:\w{3})|(?:\-{3}))\d\d\d$", v)
    if m:
        print("  OK:", v)
    else:
        print("FAIL:", v)

'''
(?:    The start of a non-capturing group.
\w{3}  Three word characters.
|      Logical or: a group within the chain must match.
\-     An escaped hyphen.
\d     A digit.
$      The end of the string.
'''
