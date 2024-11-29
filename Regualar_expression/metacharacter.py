# In regular expressions, metacharacters are characters with special meanings that help define patterns.
# Here's a rundown of some of the most common metacharacters and their types in Python regex:
#
# Common Metacharacters
# Dot (.)
#
# Matches any character except a newline.
# Example: a.b matches aab, aXb, but not ab or a\nb.
# Caret (^)
#
# Matches the start of the string.
# Example: ^Hello matches Hello world, but not A Hello world.
# Dollar ($)
#
# Matches the end of the string.
# Example: world$ matches Hello world, but not Hello world!.
# Asterisk (*)
#
# Matches 0 or more repetitions of the preceding element.
# Example: ab*c matches ac, abc, abbc, etc.
# Plus (+)
#
# Matches 1 or more repetitions of the preceding element.
# Example: ab+c matches abc, abbc, but not ac.
# Question Mark (?)
#
# Matches 0 or 1 repetition of the preceding element.
# Example: ab?c matches ac and abc, but not abbc.
# Braces ({})
#
# Matches a specified number of repetitions of the preceding element.
# Example: a{2} matches aa, a{2,3} matches aa or aaa.
# Square Brackets ([])
#
# Matches any one of the characters inside the brackets.
# Example: [abc] matches a, b, or c.
# Pipe (|)
#
# Acts as an OR operator.
# Example: a|b matches a or b.
# Parentheses (())
#
# Groups patterns together and captures the match for use.
# Example: (abc)+ matches abc, abcabc, etc.
# Character Classes
# Character classes allow for matching any one of a set of characters.
#
# \d
#
# Matches any digit (0-9).
# Equivalent to [0-9].
# \D
#
# Matches any non-digit.
# Equivalent to [^0-9].
# \w
#
# Matches any word character (alphanumeric plus underscore).
# Equivalent to [a-zA-Z0-9_].
# \W
#
# Matches any non-word character.
# Equivalent to [^a-zA-Z0-9_].
# \s
#
# Matches any whitespace character (spaces, tabs, newlines).
# Equivalent to [ \t\n\r\f\v].
# \S
#
# Matches any non-whitespace character.
# Equivalent to [^ \t\n\r\f\v].
# Special Sequences
# \b
#
# Matches a word boundary.
# Example: \bword\b matches word in word boundary, but not sword.
# \B
#
# Matches a non-word boundary.
# Example: \Bword\B matches word in swordplay, but not word boundary.



import re
string = "abc"
pattern = "ab*c"

#Asterisk (*)
#
# Matches 0 or more repetitions of the preceding element.
# Example: ab*c matches ac, abc, abbc, etc.
# if re.match(pattern,string):
#     print("Match Found")
# else:
#     print("Match not found ")
