text = str(input("Enter text: "))

if text.isupper():
    print(text[0] + text[1:].lower() + "!")
else:
    print(text)