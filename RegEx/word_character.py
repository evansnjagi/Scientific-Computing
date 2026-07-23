# word matching 
# Import
import re

text = "Hello, my name is Evans"
match = re.findall(r"\w+", text)
print(match)

# [] Character class
match_2 = re.findall(r"[a e i o u]", "Nairobi")
print(f"Match: {match_2}")

# Range inside []
match_3 = re.findall(r"[A-Z]", "My Name Is Evans")
print("Match three: ", match_3)