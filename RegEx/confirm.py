# Import
import re

text = "KE2024/001"

# Match
match = re.findall(r"\d{4}", text)

if match:
    print("Match: ", match)
else:
    print("No match found.")