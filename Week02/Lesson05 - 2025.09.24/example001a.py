"""
Determine the number of characters or letters in each word within a sentence.
"""

# Classical method
sentence = "Technology is fun and exciting. It helps us learn new things every day."

words = sentence.split()
for word in words:
    number = len(word)
    print(f"The word '{word}' has {number} characters.")

# Modern method (by list comprehension)
sentence = "Technology is fun and exciting. It helps us learn new things every day."

words = sentence.split()
print(words)

length = [len(word) for word in words]

for word, length_ in zip(words, length):
    print(word, length_)
