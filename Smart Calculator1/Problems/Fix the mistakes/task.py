words = input().split()
for word in words:
    if word.lower().startswith(("www.", "https://", "http://")):
        print(word)
