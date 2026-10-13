"""
CP1404 Prac 5: Word Occurrences
Estimate: 8 minutes
Actual: 31 minutes
"""

text = input("Text: ")
word_to_count = {}

words = text.split()
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

word_to_count = dict(sorted(word_to_count.items()))

width = max(len(word) for word in word_to_count)

for word, count in word_to_count.items():
    print(f"{word:{width}} : {count}")
