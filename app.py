def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted = ord(char) + shift_amount
                if shifted > ord('z'):
                    shifted -= 26
                result += chr(shifted)
            elif char.isupper():
                shifted = ord(char) + shift_amount
                if shifted > ord('Z'):
                    shifted -= 26
                result += chr(shifted)
        else:
            result += char
    return result

print(caesar_cipher("Hello, World!", 3))
