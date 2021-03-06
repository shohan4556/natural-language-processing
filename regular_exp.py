import re 

text = 'abcded efgh'
my_string = "Let's write RegEx!"

#match start searching from beginning 
print(re.match(r'abc', text))
# return None 
print(re.match(r'efg', text))

#search will go through the entire string 
print(re.search(r'efg', text))

print(re.split(r'a', text))

# find all words 
print(re.findall(r'\w*', my_string))

my_string = "Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?"

# Write a pattern to match sentence endings: sentence_endings
sentence_endings = r"[.?!]"

# Split my_string on sentence endings and print the result
print(re.split(sentence_endings, my_string))

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, my_string))

# Split my_string on spaces and print the result
spaces = r"\s+"
print(re.split(spaces, my_string))

# Find all digits in my_string and print the result
digits = r"\d+"
print(re.findall(digits, my_string))

# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = r"\[.*]+"

# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"[A-z]+:"

