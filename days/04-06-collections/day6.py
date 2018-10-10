from collections import Counter
import string

with open("harry.txt") as f:
    text = f.read()
text = text.lower()
words_with_punct = text.split()
words = [word.strip(string.punctuation) for word in words_with_punct]
word_count = Counter(words)
del word_count[""]
common = word_count.most_common(20)
for word in common:
    print(f"{word[0]}: {word[1]}")
