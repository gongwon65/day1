import re
text="""
park 010-9999-9998
kim 010-9909-7789
lee 010-8789-7768
"""

modified_text = re.sub(r"(\d{3}-\d{4})-\d{4}", r'\1-####', text)

print(modified_text)