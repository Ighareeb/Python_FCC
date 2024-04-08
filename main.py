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
