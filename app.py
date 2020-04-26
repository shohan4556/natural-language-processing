import re 

text = 'abcded efgh'
my_string = "Let's write RegEx!"

print(re.match('abc', text))
print(re.split('a', text))
print(re.findall('\w+', my_string))