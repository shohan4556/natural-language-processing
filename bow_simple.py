# Import Counter
from collections import Counter 
from nltk.tokenize import word_tokenize


article = 'this is a demo article, demo article of wikipedia'

# Tokenize the article: tokens
tokens = word_tokenize(article)
print(type(tokens))

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [i.lower() for i in tokens]

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)

# Print the 10 most common tokens
print(bow_simple.most_common(2))
