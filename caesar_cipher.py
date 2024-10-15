# Caesar Cipher

# Create a function that takes two arguments (text, key) and returns a new encrypted text using the key.
# For example, if the input is "a" and the key is 1, it should move that letter 1 step in alphabetic order so the output would be "b".
# Examples

# caesar_cipher("hello", 5) ➞ "mjqqt"

# caesar_cipher("hello world", 1) ➞ "ifmmp xpsme"

# caesar_cipher("a", 2) ➞ "c"

# Notes

# The input is only letters and spaces; no special characters.



def caesar_cipher(text, key):
    result = ""
    
    for char in text:
        if char.isalpha():  # Check if it's a letter
            shift = ord('A') if char.isupper() else ord('a')  # Determine if it's upper or lowercase
            # Shift the character and wrap around the alphabet using modulo
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char  # Keep spaces unchanged
    
    return result

# Test cases
print(caesar_cipher("hello", 5))          # Expected: "mjqqt"
print(caesar_cipher("hello world", 1))    # Expected: "ifmmp xpsme"
print(caesar_cipher("a", 2))              # Expected: "c"
