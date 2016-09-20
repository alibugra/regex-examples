import re

m = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{10,}$')

print(m.match('43543fooR')) # None
print(m.match('43543fooRy').string)
print(m.match('foobar7678A').string)
print(m.match('foobar76(')) # None
print(m.match('fokhjf7645464644sresrtf')) # None
print(m.match('fokhjf764546M4644sresrtf').string)

'''
(?=.*?\d) Checks for atleast one digit
(?=.*?[A-Z]) Atleast one uppercsae.
(?=.*?[a-z]) Atleast one lowercase.
[A-Za-z\d]{10,} Matches uppercase or lowercase or digit characters 10 or more times. This ensures that the match must have atleast 10 characters.
'''

'''
The requirements for my password are:
at least 10 symbols
at least one digit
at least one uppercase letter
at least one lowercase letter
only letters or digits
'''
