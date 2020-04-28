# Import the necessary modules
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import regexp_tokenize

tweets = 'This is the best #nlp exercise ive found online! #python', '#NLP is super fun! <3 #learning', 'Thanks @datacamp :) #nlp #python'

#find hashtag
#start with #, word, all(greed)
#print(len(tweets))
pattern1 = r"#\w+"
hashtag = regexp_tokenize(tweets[0], pattern1)
print(hashtag)

# Write a pattern that matches both mentions (@) and hashtags
pattern2 = r"([\@\#]\w+)"
# Use the pattern on the last tweet in the tweets list
mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
print(mentions_hashtags)

#twiiter tokenizer 
tk = TweetTokenizer()
for i in tweets:
    all_tokens = tk.tokenize(i)
    print(all_tokens)

