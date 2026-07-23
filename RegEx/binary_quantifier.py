# The ? quantifier
# Import 
import re

# Text
words = ["color", "colour"]

# Loop
for w in words:
    # Match
    match = re.fullmatch(r"colou?r", w)

    # Validate match
    print(f"'{w}' -> {'match' if match else 'no match'}")
