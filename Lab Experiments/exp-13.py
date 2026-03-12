import string
from collections import Counter

reviews = [
    "This product is excellent and very useful",
    "Excellent quality and great performance",
    "The product quality is good and useful",
    "Very good product with excellent features",
    "Good quality and great value"
]

all_text = " ".join(reviews).lower()

translator = str.maketrans("", "", string.punctuation)
cleaned_text = all_text.translate(translator)

words = cleaned_text.split()

word_frequency = Counter(words)

print("Word Frequency Distribution:")
for word, frequency in word_frequency.most_common():
    print(word, ":", frequency)
