# Import 
import re

# Text
texts = [
    "price is 5",
    "price is 150",
    "price is 3400",
    "price is 1000000",
    "no price here",
]

# Match
for t in texts:
    # Greedy search
    match = re.search(r"\d+", t)
    
    if match:
        print("Match found in '{}': {} at position {}".format(t, match.group(), match.span()))
    else:
        print("No match found in '{}'.".format(t))