# Strings

text = "X-DSPAM-Confidence:    0.8475"
index=text.find(':')
number=float(text[index+1:])
print(number)
