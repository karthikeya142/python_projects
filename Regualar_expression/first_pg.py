#Regular expressions (regex) are a powerful tool in Python for matching patterns in strings.
# The re module in Python provides support for working with regular expressions.
# Here are some common tasks and examples of how to use regex in Python:

import re
string = input("Enter a string: ")
pattern = input("Enter pattren: ")
#To check if a string matches a pattern, use the re.match() function.
# It checks for a match only at the beginning of the string.

# if re.match(pattern,string):
#     print("Match Found")
# else:
#     print("Match not found ")

#To search for a pattern anywhere in the string, use re.search().

# if re.search(pattern,string):
#     print("Match Found")
# else:
#     print("Match not found ")

#To find all occurrences of a pattern, use re.findall()

pattern = r'\d+'
text = 'There are 3 apples and 4 oranges.'
matches = re.findall(pattern, text)

print("Matches found:", matches)


#  Using Special Characters
# Regular expressions use special characters for various purposes:
#
# . - Any character except a newline
# ^ - Start of the string
# $ - End of the string
# * - 0 or more repetitions
# + - 1 or more repetitions
# ? - 0 or 1 repetition
# {} - Specific number of repetitions
# [] - Any character inside the brackets
# | - OR operator