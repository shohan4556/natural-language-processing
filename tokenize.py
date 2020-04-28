# Import necessary modules
from nltk.tokenize import sent_tokenize 
from nltk.tokenize import word_tokenize

scene_one = "KING ARTHUR: Whoa there!  [clop clop clop]"
#print(scene_one)

# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[0])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

print(unique_tokens)
