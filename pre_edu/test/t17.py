import re
pattern = r'a[.]{3,}b'
strings = 'acccb','a....b','aaab','a.cccb'

matching_string = [s for s in strings if re.match(pattern,s)]

print(matching_string)



