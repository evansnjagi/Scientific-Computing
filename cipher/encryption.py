# Encrypting using Caesar cipher method
text = "Hello, Zorld"
shift = 3

def cipher(text, shift):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = str()
    for char in text.lower():
        if char == " ":
            encrypted_text += char
        elif char == ",":
            encrypted_text += char
        else:
            position = alphabets.find(char)
            new_position = position + shift
            encrypted_text += alphabets[(new_position) % 26]
    return encrypted_text

encrypted_text = cipher(text, shift)
print("Normal: ", text, "\n","Encrypted: ", encrypted_text)
