# Import necessary modules
from nltk.tokenize import sent_tokenize, word_tokenize


scene_one = "All work and no play makes jack a dull boy, all work and no play"
#print(scene_one)
print(word_tokenize(scene_one))

# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[0])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

print(unique_tokens)
