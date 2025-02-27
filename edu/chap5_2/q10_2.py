#Q10
text = "hello world, this is a python example."
text_split = text.split(' ')
text_cap = []
for x in text_split:
    text_cap.append(x.capitalize())
text_join = ' '.join(text_cap)
print(text_join)