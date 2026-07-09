# Import 
import re

# Data
prices = [
    "Total: KES 500",
    "Total: KES 500.75",
    "Total: KES 1200.5",
    "Total: KES 0",
]

# Loop
for p in prices:
    # Match
    match = re.search(r"\d+\.\d*", p)

    if match:
        print(match.group())
    else:
        print(f"{p} -> No match")