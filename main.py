# # --------------------------------TUTORIAL 1---------------------------------------------------
# # Caeser cipher - Encryption
# # take letter from message --> find position in alphabet --> replace with letter 3+ positions ahead
# text = "Hello World"
# shift = 3


# def caesar(message, offset):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"

#     encrypted_text = ""

#     for char in message.lower():
#         if char == " ":
#             # print('space!') # since a space would be 0 + 3 it would print as 'c', use else clause to print space instead
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             # print(char, index)
#             new_index = (index + offset) % len(
#                 alphabet
#             )  # handling --> index + shift > 26/len(alphabet) in case alphabet variable modified
#             # new_char = alphabet[new_index]
#             # print(new_char)
#             encrypted_text += alphabet[new_index]
#         # print('char:', char, 'encrypted text:', encrypted_text)
#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)


# caesar(text, shift)
# caesar(text, 13)

# # -----------------------------------------------------------------------------------
# # Vigenère Cipher (encrypt, decrypt fucntionality + punctuation/special chars/digits )
# # offset for each letter is determined by another text, called the key
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     # *note: since key is shorter than text --> need to repeat it until it matches the length of the text
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # if char == " ": # replaced with --> .isalpha() method to check if char is NOT a letter/alphabetic-characters instead
#         # Append to message now includes punctuation, special chars, digits etc. (not just spaces)
#         if not char.isalpha():
#             encrypted_text += char
#         else:
#             # find correct key_char to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define offset and encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             # new_index = (index + offset) % len(alphabet)
#             # add decrpytion functionality by multiplying offset by direction (1 encrypt / -1 decrypt)
#             new_index = (index + (offset * direction)) % len(alphabet)
#             encrypted_text += alphabet[new_index]
#     return encrypted_text


# # for encryption don't need to specify direction, default is 1
# def encrypt(message, key):
#     return vigenere(message, key)


# def decrypt(message, key):
#     return vigenere(message, key, -1)


# encryption = encrypt(text, custom_key)
# print(encryption)
# decryption = decrypt(encryption, custom_key)
# print(decryption)


# # encryption = vigenere(text, custom_key, 1)
# # print(encryption)
# # decryption = vigenere(encryption, custom_key, -1)
# # print(decryption)


# # --------------------------------TUTORIAL 2---------------------------------------------------
# # Luhn Algorithm - check notes
# def luhn_algo(number):
#     sum_of_odd_digits = 0
#     card_number_reversed = number[::-1]
#     odd_digits = card_number_reversed[::2]
#     print(odd_digits)
#     for digit in odd_digits:
#         sum_of_odd_digits += int(digit)
#         print(sum_of_odd_digits)
#     # 1. from R --> L double every second digit; if > 9 then sum the digits of product (eg. 6*2=12 sum = 1+2=3)
#     sum_of_even_digits = 0
#     even_digits = card_number_reversed[1::2]
#     for digit in even_digits:
#         number = int(digit) * 2
#         sum_of_even_digits += number
#         if number >= 10:
#             number = number // 10 + number % 10
#         sum_of_even_digits += number
#     # 2.Take the sum of all the digits.
#     # --> 3. if [2.sum] is multiple of 10 (number is vald) else (number invalid)
#     total = sum_of_odd_digits + sum_of_even_digits
#     return 0 == total % 10


# def verify_card_number():
#     card_number = "4111-1111-4555-1142"
#     card_translation = str.maketrans({"-": "", " ": ""})
#     translated_card_number = card_number.translate(card_translation)

#     if luhn_algo(translated_card_number):
#         print("Valid")
#     else:
#         print("Invalid")
#     print(translated_card_number)


# verify_card_number()


# # --------------------------------TUTORIAL 3---------------------------------------------------
# # Lambda functions - (create expense tracker)
# def main():
#     expenses = []
#     while True:
#         print("\nExpense Tracker")
#         print("1. Add an expense")
#         print("2. List all expenses")
#         print("3. Show total expenses")
#         print("4. Filter expenses by category")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             amount = float(input("Enter amount: "))
#             category = input("Enter category: ")
#             add_expense(expenses, amount, category)

#         elif choice == "2":
#             print("\nAll Expenses:")
#             print_expenses(expenses)

#         elif choice == "3":
#             print("\nTotal Expenses: ", total_expenses(expenses))

#         elif choice == "4":
#             category = input("Enter category to filter: ")
#             print(f"\nExpenses for {category}:")
#             expenses_from_category = filter_expenses_by_category(expenses, category)
#             print_expenses(expenses_from_category)

#         elif choice == "5":
#             print("Exiting the program.")
#             break


# def add_expense(expenses, amount, category):
#     expenses.append({"amount": amount, "category": category})


# def print_expenses(expenses):
#     for expense in expenses:
#         print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


# def total_expenses(expenses):
#     return sum(map(lambda expense: expense["amount"], expenses))


# def filter_expenses_by_category(expenses, category):
#     return filter(lambda expense: expense["category"] == category, expenses)


# # check to see if main is being run as the main program i.e. script running directly; not imported
# if __name__ == "__main__":
#     main()

# # --------------------------------TUTORIAL 4---------------------------------------------------
# # List Comprehension - (construct new list from iterable types + str Format Case-converter) [without using FOR loop or .append()]


# # (v1 FOR LOOP) utility function to convert string to snake_case
# def convert_to_snake_case_for_loop(pascal_or_camel_cased_string):
#     snake_cased_char_list = []
#     for char in pascal_or_camel_cased_string:
#         if char.isupper():
#             converted_character = "_" + char.lower()
#             snake_cased_char_list.append(converted_character)
#         else:
#             snake_cased_char_list.append(char)
#     snake_cased_string = "".join(snake_cased_char_list)
#     clean_snake_cased_string = snake_cased_string.strip(
#         "_"
#     )  # remove '_' from start/end
#     return clean_snake_cased_string


# # (v2 LIST COMPREHENSION) utility function to convert string to snake_case
# def convert_to_snake_case(pascal_or_camel_cased_string):
#     # In the list constructor -->describe how build list based on conditions
#     snake_cased_char_list = [
#         # write condition first then object to iterate over
#         "_" + char.lower() if char.isupper() else char
#         for char in pascal_or_camel_cased_string
#     ]
#     return "".join(snake_cased_char_list).strip("_")


# def main():
#     print(convert_to_snake_case_for_loop("aLongAndComplexString"))
#     print(convert_to_snake_case("IAmAPascalCasedString"))


# if __name__ == "__main__":
#     main()

# --------------------------------TUTORIAL 5---------------------------------------------------
# Tutorial 5: Regular Expressions - Build Password Generator
import string

# import random ## use secrets instead of random for more secure random number generation
import secrets
import re  # regular expressions


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # these 3 variables consitute the pool of characters that can be used to generate a password
    letters = string.ascii_letters  # lower then upper case letters
    digits = string.digits
    symbols = string.punctuation
    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ""
        # Generate password
        # note '_' used to represent variable you don't care about/won't use in your code. (i.e. iteration value not actually being used, just want to functionality of FOR LOOP)
        for _ in range(length):
            password += secrets.choice(all_characters)

        # Check Constraints
        constraints = [
            (nums, r"\d"),
            (lowercase, r"[a-z]"),
            (uppercase, r"[A-Z]"),
            (special_chars, rf"[{symbols}]"),
        ]

        # count = 0
        # for constraint, pattern in constraints:
        #     if constraint <= len(re.findall(pattern, password)):
        #         count += 1

        #     if count == 4:
        ## replace with comprehension syntax and all() function which returns True if all items in iterable are True
        # if all(
        #     [
        #         constraint <= len(re.findall(pattern, password))
        #         for constraint, pattern in constraints
        #     ]
        # ):
        # # modify again to make it a generator expression instead of list comprehension (use () instead of []) --> more memory efficient
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    return password


if __name__ == "__main__":
    new_password = generate_password(
        10,
        1,
        1,
        1,
        1,
    )
    print("Generated password:", new_password)


# --------------------------------TUTORIAL 6---------------------------------------------------
# Tutorial 6: Algorithm Desgin - Shortest Path Algo
# #(eg. For Graph Data structures - Dijkstra's Algorithm)
my_graph_non_weighted = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["A", "C"],
}
# Create weighted dict extending example - modify dict using list of tuples for each value first element in tuple = connected node, second element = weight of edge
my_graph_weighted = {
    "A": [("B", 3), ("D", 1)],
    "B": [("A", 3), ("C", 4)],
    "C": [("B", 4), ("D", 7)],
    "D": [("A", 1), ("C", 7)],
}
my_graph_weighted_2 = {
    "A": [("B", 5), ("C", 3), ("E", 11)],
    "B": [("A", 5), ("C", 1), ("F", 2)],
    "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 9), ("F", 3)],
    "E": [("A", 11), ("C", 5), ("D", 9)],
    "F": [("B", 2), ("D", 3)],
}


# Algo will start at specific node, then explore all possible paths from that node to find the shortest path to any of the other nodes
def shortest_path(graph, start, target=""):
    # track visited nodes - explore all nodes connected to start and calculate shortest path then remove start node and repeast process for closest neighbour etc.
    unvisited_node = list(graph)
    # track shortest distance to each node
    distances = {node: 0 if node == start else float("inf") for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(
        start
    )  # returns in alphabetical order --> we want smallest distance (while loop param)
    while unvisited_node:
        current = min(
            unvisited_node, key=distances.get
        )  # define current node to visit *note pylance error but code words...don't want to use lambda function workaround for now just for typecheck
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                # keep track of node as distances dict updated (appended so is last item)
                if paths[node] and paths[node][-1] == node:
                    # if shorter distance is found avoid assigning the same path to the node. (use copy of current path to avoid modifying original path list)
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(
                        paths[current]
                    )  # add the current node path to the neighbor node path
                paths[node].append(node)
        unvisited_node.remove(current)

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue  # skip start node
        print(
            f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}'
        )
    return distances, paths

    print(f"Unvisited: {unvisited_node}\nDistances: {distances}\nPaths: {paths}")


# for node in graph:
# unvisited_node.append(node)
# if node == start:
#     distances[node] = 0
# # initially all other nodes considered to be infinite distance from start node
# else:
#     distances[node] = float("inf")


shortest_path(my_graph_weighted, "A")  # can add 3rd param to specify target node
# >>> Unvisited: ['A', 'B', 'C', 'D']
# Distances: {'A': 0, 'B': inf, 'C': inf, 'D': inf}
# Paths: {'A': ['A'], 'B': [], 'C': [], 'D': []}
# >>>
# A-A distance: 0
# Path: A
# >>>
# A-B distance: 3
# Path: A -> B
# >>>
# A-C distance: 7
# Path: A -> B -> C
# >>>
# A-D distance: 1
# Path: A -> D
