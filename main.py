# Caeser cipher - Encryption
# take letter from message --> find position in alphabet --> replace with letter 3+ positions ahead
text = "Hello World"
shift = 3


def caesar(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    encrypted_text = ""

    for char in message.lower():
        if char == " ":
            # print('space!') # since a space would be 0 + 3 it would print as 'c', use else clause to print space instead
            encrypted_text += char
        else:
            index = alphabet.find(char)
            # print(char, index)
            new_index = (index + offset) % len(
                alphabet
            )  # handling --> index + shift > 26/len(alphabet) in case alphabet variable modified
            # new_char = alphabet[new_index]
            # print(new_char)
            encrypted_text += alphabet[new_index]
        # print('char:', char, 'encrypted text:', encrypted_text)
    print("plain text:", message)
    print("encrypted text:", encrypted_text)


caesar(text, shift)
caesar(text, 13)

# -----------------------------------------------------------------------------------
# Vigenère Cipher (encrypt, decrypt fucntionality + punctuation/special chars/digits )
# offset for each letter is determined by another text, called the key
custom_key = "python"


def vigenere(message, key, direction=1):
    key_index = 0
    # *note: since key is shorter than text --> need to repeat it until it matches the length of the text
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""

    for char in message.lower():
        # if char == " ": # replaced with --> .isalpha() method to check if char is NOT a letter/alphabetic-characters instead
        # Append to message now includes punctuation, special chars, digits etc. (not just spaces)
        if not char.isalpha():
            encrypted_text += char
        else:
            # find correct key_char to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            # Define offset and encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            # new_index = (index + offset) % len(alphabet)
            # add decrpytion functionality by multiplying offset by direction (1 encrypt / -1 decrypt)
            new_index = (index + (offset * direction)) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text


# for encryption don't need to specify direction, default is 1
def encrypt(message, key):
    return vigenere(message, key)


def decrypt(message, key):
    return vigenere(message, key, -1)


encryption = encrypt(text, custom_key)
print(encryption)
decryption = decrypt(encryption, custom_key)
print(decryption)


# encryption = vigenere(text, custom_key, 1)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)


# -----------------------------------------------------------------------------------
