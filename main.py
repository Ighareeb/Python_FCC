# --------------------------------TUTORIAL 1---------------------------------------------------
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


# --------------------------------TUTORIAL 2---------------------------------------------------
# Luhn Algorithm - check notes
def luhn_algo(number):
    sum_of_odd_digits = 0
    card_number_reversed = number[::-1]
    odd_digits = card_number_reversed[::2]
    print(odd_digits)
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
        print(sum_of_odd_digits)
    # 1. from R --> L double every second digit; if > 9 then sum the digits of product (eg. 6*2=12 sum = 1+2=3)
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        sum_of_even_digits += number
        if number >= 10:
            number = number // 10 + number % 10
        sum_of_even_digits += number
    # 2.Take the sum of all the digits.
    # --> 3. if [2.sum] is multiple of 10 (number is vald) else (number invalid)
    total = sum_of_odd_digits + sum_of_even_digits
    return 0 == total % 10


def verify_card_number():
    card_number = "4111-1111-4555-1142"
    card_translation = str.maketrans({"-": "", " ": ""})
    translated_card_number = card_number.translate(card_translation)

    if luhn_algo(translated_card_number):
        print("Valid")
    else:
        print("Invalid")
    print(translated_card_number)


verify_card_number()


# --------------------------------TUTORIAL 3---------------------------------------------------
# Lambda functions - (create expense tracker)
def main():
    expenses = []
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Show total expenses")
        print("4. Filter expenses by category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(expenses, amount, category)

        elif choice == "2":
            print("\nAll Expenses:")
            print_expenses(expenses)

        elif choice == "3":
            print("\nTotal Expenses: ", total_expenses(expenses))

        elif choice == "4":
            category = input("Enter category to filter: ")
            print(f"\nExpenses for {category}:")
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == "5":
            print("Exiting the program.")
            break


def add_expense(expenses, amount, category):
    expenses.append({"amount": amount, "category": category})


def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


def total_expenses(expenses):
    return sum(map(lambda expense: expense["amount"], expenses))


def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense["category"] == category, expenses)


# check to see if main is being run as the main program i.e. script running directly; not imported
if __name__ == "__main__":
    main()
