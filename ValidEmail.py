import re

text = "Contact us at info@nlp.com"

list = text.split(' ')

for element in list:
    m = re.match("\w+@\w+\.(?:com|net)", element)
    if m:
        print(m.group(0))
