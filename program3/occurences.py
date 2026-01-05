text=input("enter a line of text")
words=text.split()
for word in words:
    print(word,":",words.count(word))
