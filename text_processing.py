from nltk.stem import WordNetLemmatizer
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

article = 'Anyway, what\'s so terrible about a women, women wearing pants?'
token = word_tokenize(article)

lower_token = [i.lower() for i in token]
#print(lower_token)

# Retain alphabetic words: alpha_only
alpha_only = []

for i in lower_token:
    if i.isalpha():
        alpha_only.append(i)

#print(alpha_only)

# Remove all stop words: no_stops
no_stops = []
english_stop = stopwords.words('english')

for t in alpha_only:
    if t not in english_stop:
        no_stops.append(t)

#instantiate wordnet lemmatizer 
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = []
for i in no_stops:
    lemmatized.append(wordnet_lemmatizer.lemmatize(i))

bow = Counter(lemmatized)
print(bow.most_common(2))

