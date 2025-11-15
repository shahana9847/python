words = input("Enter words: ").split()
longest = max(words, key=len)
print("Length:", len(longest))