banned_words = [
    'blin',
    'wai',
    ]

text = input("Please enter text: ")

for banned_word in banned_words:
    text = text.replace(banned_word, "*" * len(banned_word))

print(text)