message = input('>')
words = message.split(' ')
output = ''

emojis = {
    ":)": "😀",
    ":(": "🙁"
}

for word in words:
    output += emojis.get(word, word) + " "

print(words)
print(output)
