# Import
import re

# Text
text = [
    "Room 4B",
    "Floor 12",
    "No numbers here",
]

# Match
for t in text:
    # Match numbers in each string of text
    match = re.search(r"\d", t)
    
    if match:
        print(f"Match found in '{t}': {match.group()} at position {match.span()}")
    else:
        print(f"No match found in '{t}'.")