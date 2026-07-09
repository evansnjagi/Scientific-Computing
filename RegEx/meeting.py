# Introduction to Regular Expression
# A pattern is a rule defining a set of strings.

# Import 
import re

# Text
text = "The meeting is in Nairobi on Monday."

# Match the word "Nairobi"
match = re.search(r"Nairobi", text)

# Print the match
if match:
    print("Match: ", match.group())
    print("Span: ", match.span())
    print("Length of the match: ", match.end() - match.start())
else:
    print("No match found.")