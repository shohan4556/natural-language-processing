# Import the necessary modules
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import pandas as pd 


df = pd.read_csv('fake_or_real_news.csv')

# Print the head of df
print(df.head())

# Create a series to store the labels: y
y = df.label

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], y, test_size=0.33, random_state=53)

# Initialize a CountVectorizer object: count_vectorizer
count_vectorizer = CountVectorizer(stop_words='english')

# Fit the training data and then return the matrix
count_train = count_vectorizer.fit_transform(X_train)

# Transform testing data and return the matrix.
# Note we are not fitting the testing data into the CountVectorizer()
count_test = count_vectorizer.transform(X_test)

# Print the first 10 features of the count_vectorizer
print(count_vectorizer.get_feature_names()[:10])

#simple and effective model 
nb_classifier = MultinomialNB()

nb_classifier.fit(count_train, y_train)

pred = nb_classifier.predict(count_test)

accu = metrics.accuracy_score(y_test, pred)

print(accu)

print(metrics.confusion_matrix(y_test, pred))
