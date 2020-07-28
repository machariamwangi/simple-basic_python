message = input(">")
words = message.split(' ')
emojis = {
    ":)": "happy emoji",
    ":(": "Sad emoji"
}
output = ""
for word in words:
   output += emojis.get(word, word) + " "
   print(output)
