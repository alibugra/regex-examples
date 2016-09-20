import re

# Input.
value = "voorheesville"

m = re.search("(vi.*)", value)
if m:
    # This is reached.
    print("search:", m.group(1))

m = re.match("(vi.*)", value)
if m:
    # This is not reached.
    print("match:", m.group(1))

'''
Pattern: (vi.*)

vi       The lowercase letters v and i together.
.*       Zero or more characters of any type.
'''
