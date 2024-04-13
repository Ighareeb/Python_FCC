# # # --------------------------------TUTORIAL 1---------------------------------------------------
# # # Caeser cipher - Encryption
# # # take letter from message --> find position in alphabet --> replace with letter 3+ positions ahead
# # text = "Hello World"
# # shift = 3


# # def caesar(message, offset):
# #     alphabet = "abcdefghijklmnopqrstuvwxyz"

# #     encrypted_text = ""

# #     for char in message.lower():
# #         if char == " ":
# #             # print('space!') # since a space would be 0 + 3 it would print as 'c', use else clause to print space instead
# #             encrypted_text += char
# #         else:
# #             index = alphabet.find(char)
# #             # print(char, index)
# #             new_index = (index + offset) % len(
# #                 alphabet
# #             )  # handling --> index + shift > 26/len(alphabet) in case alphabet variable modified
# #             # new_char = alphabet[new_index]
# #             # print(new_char)
# #             encrypted_text += alphabet[new_index]
# #         # print('char:', char, 'encrypted text:', encrypted_text)
# #     print("plain text:", message)
# #     print("encrypted text:", encrypted_text)


# # caesar(text, shift)
# # caesar(text, 13)

# # # -----------------------------------------------------------------------------------
# # # Vigenère Cipher (encrypt, decrypt fucntionality + punctuation/special chars/digits )
# # # offset for each letter is determined by another text, called the key
# # custom_key = "python"


# # def vigenere(message, key, direction=1):
# #     key_index = 0
# #     # *note: since key is shorter than text --> need to repeat it until it matches the length of the text
# #     alphabet = "abcdefghijklmnopqrstuvwxyz"
# #     encrypted_text = ""

# #     for char in message.lower():
# #         # if char == " ": # replaced with --> .isalpha() method to check if char is NOT a letter/alphabetic-characters instead
# #         # Append to message now includes punctuation, special chars, digits etc. (not just spaces)
# #         if not char.isalpha():
# #             encrypted_text += char
# #         else:
# #             # find correct key_char to encode/decode
# #             key_char = key[key_index % len(key)]
# #             key_index += 1
# #             # Define offset and encrypted/decrypted letter
# #             offset = alphabet.index(key_char)
# #             index = alphabet.find(char)
# #             # new_index = (index + offset) % len(alphabet)
# #             # add decrpytion functionality by multiplying offset by direction (1 encrypt / -1 decrypt)
# #             new_index = (index + (offset * direction)) % len(alphabet)
# #             encrypted_text += alphabet[new_index]
# #     return encrypted_text


# # # for encryption don't need to specify direction, default is 1
# # def encrypt(message, key):
# #     return vigenere(message, key)


# # def decrypt(message, key):
# #     return vigenere(message, key, -1)


# # encryption = encrypt(text, custom_key)
# # print(encryption)
# # decryption = decrypt(encryption, custom_key)
# # print(decryption)


# # # encryption = vigenere(text, custom_key, 1)
# # # print(encryption)
# # # decryption = vigenere(encryption, custom_key, -1)
# # # print(decryption)


# # # --------------------------------TUTORIAL 2---------------------------------------------------
# # # Luhn Algorithm - check notes
# # def luhn_algo(number):
# #     sum_of_odd_digits = 0
# #     card_number_reversed = number[::-1]
# #     odd_digits = card_number_reversed[::2]
# #     print(odd_digits)
# #     for digit in odd_digits:
# #         sum_of_odd_digits += int(digit)
# #         print(sum_of_odd_digits)
# #     # 1. from R --> L double every second digit; if > 9 then sum the digits of product (eg. 6*2=12 sum = 1+2=3)
# #     sum_of_even_digits = 0
# #     even_digits = card_number_reversed[1::2]
# #     for digit in even_digits:
# #         number = int(digit) * 2
# #         sum_of_even_digits += number
# #         if number >= 10:
# #             number = number // 10 + number % 10
# #         sum_of_even_digits += number
# #     # 2.Take the sum of all the digits.
# #     # --> 3. if [2.sum] is multiple of 10 (number is vald) else (number invalid)
# #     total = sum_of_odd_digits + sum_of_even_digits
# #     return 0 == total % 10


# # def verify_card_number():
# #     card_number = "4111-1111-4555-1142"
# #     card_translation = str.maketrans({"-": "", " ": ""})
# #     translated_card_number = card_number.translate(card_translation)

# #     if luhn_algo(translated_card_number):
# #         print("Valid")
# #     else:
# #         print("Invalid")
# #     print(translated_card_number)


# # verify_card_number()


# # # --------------------------------TUTORIAL 3---------------------------------------------------
# # # Lambda functions - (create expense tracker)
# # def main():
# #     expenses = []
# #     while True:
# #         print("\nExpense Tracker")
# #         print("1. Add an expense")
# #         print("2. List all expenses")
# #         print("3. Show total expenses")
# #         print("4. Filter expenses by category")
# #         print("5. Exit")

# #         choice = input("Enter your choice: ")

# #         if choice == "1":
# #             amount = float(input("Enter amount: "))
# #             category = input("Enter category: ")
# #             add_expense(expenses, amount, category)

# #         elif choice == "2":
# #             print("\nAll Expenses:")
# #             print_expenses(expenses)

# #         elif choice == "3":
# #             print("\nTotal Expenses: ", total_expenses(expenses))

# #         elif choice == "4":
# #             category = input("Enter category to filter: ")
# #             print(f"\nExpenses for {category}:")
# #             expenses_from_category = filter_expenses_by_category(expenses, category)
# #             print_expenses(expenses_from_category)

# #         elif choice == "5":
# #             print("Exiting the program.")
# #             break


# # def add_expense(expenses, amount, category):
# #     expenses.append({"amount": amount, "category": category})


# # def print_expenses(expenses):
# #     for expense in expenses:
# #         print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


# # def total_expenses(expenses):
# #     return sum(map(lambda expense: expense["amount"], expenses))


# # def filter_expenses_by_category(expenses, category):
# #     return filter(lambda expense: expense["category"] == category, expenses)


# # # check to see if main is being run as the main program i.e. script running directly; not imported
# # if __name__ == "__main__":
# #     main()

# # # --------------------------------TUTORIAL 4---------------------------------------------------
# # # List Comprehension - (construct new list from iterable types + str Format Case-converter) [without using FOR loop or .append()]


# # # (v1 FOR LOOP) utility function to convert string to snake_case
# # def convert_to_snake_case_for_loop(pascal_or_camel_cased_string):
# #     snake_cased_char_list = []
# #     for char in pascal_or_camel_cased_string:
# #         if char.isupper():
# #             converted_character = "_" + char.lower()
# #             snake_cased_char_list.append(converted_character)
# #         else:
# #             snake_cased_char_list.append(char)
# #     snake_cased_string = "".join(snake_cased_char_list)
# #     clean_snake_cased_string = snake_cased_string.strip(
# #         "_"
# #     )  # remove '_' from start/end
# #     return clean_snake_cased_string


# # # (v2 LIST COMPREHENSION) utility function to convert string to snake_case
# # def convert_to_snake_case(pascal_or_camel_cased_string):
# #     # In the list constructor -->describe how build list based on conditions
# #     snake_cased_char_list = [
# #         # write condition first then object to iterate over
# #         "_" + char.lower() if char.isupper() else char
# #         for char in pascal_or_camel_cased_string
# #     ]
# #     return "".join(snake_cased_char_list).strip("_")


# # def main():
# #     print(convert_to_snake_case_for_loop("aLongAndComplexString"))
# #     print(convert_to_snake_case("IAmAPascalCasedString"))


# # if __name__ == "__main__":
# #     main()

# # --------------------------------TUTORIAL 5---------------------------------------------------
# # Tutorial 5: Regular Expressions - Build Password Generator
# import string

# # import random ## use secrets instead of random for more secure random number generation
# import secrets
# import re  # regular expressions


# def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
#     # these 3 variables consitute the pool of characters that can be used to generate a password
#     letters = string.ascii_letters  # lower then upper case letters
#     digits = string.digits
#     symbols = string.punctuation
#     # Combine all characters
#     all_characters = letters + digits + symbols

#     while True:
#         password = ""
#         # Generate password
#         # note '_' used to represent variable you don't care about/won't use in your code. (i.e. iteration value not actually being used, just want to functionality of FOR LOOP)
#         for _ in range(length):
#             password += secrets.choice(all_characters)

#         # Check Constraints
#         constraints = [
#             (nums, r"\d"),
#             (lowercase, r"[a-z]"),
#             (uppercase, r"[A-Z]"),
#             (special_chars, rf"[{symbols}]"),
#         ]

#         # count = 0
#         # for constraint, pattern in constraints:
#         #     if constraint <= len(re.findall(pattern, password)):
#         #         count += 1

#         #     if count == 4:
#         ## replace with comprehension syntax and all() function which returns True if all items in iterable are True
#         # if all(
#         #     [
#         #         constraint <= len(re.findall(pattern, password))
#         #         for constraint, pattern in constraints
#         #     ]
#         # ):
#         # # modify again to make it a generator expression instead of list comprehension (use () instead of []) --> more memory efficient
#         if all(
#             constraint <= len(re.findall(pattern, password))
#             for constraint, pattern in constraints
#         ):
#             break
#     return password


# if __name__ == "__main__":
#     new_password = generate_password(
#         10,
#         1,
#         1,
#         1,
#         1,
#     )
#     print("Generated password:", new_password)


# # --------------------------------TUTORIAL 6---------------------------------------------------
# # Tutorial 6: Algorithm Desgin - Shortest Path Algo
# # #(eg. For Graph Data structures - Dijkstra's Algorithm)
# my_graph_non_weighted = {
#     "A": ["B", "D"],
#     "B": ["A", "C"],
#     "C": ["B", "D"],
#     "D": ["A", "C"],
# }
# # Create weighted dict extending example - modify dict using list of tuples for each value first element in tuple = connected node, second element = weight of edge
# my_graph_weighted = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }
# my_graph_weighted_2 = {
#     "A": [("B", 5), ("C", 3), ("E", 11)],
#     "B": [("A", 5), ("C", 1), ("F", 2)],
#     "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
#     "D": [("C", 1), ("E", 9), ("F", 3)],
#     "E": [("A", 11), ("C", 5), ("D", 9)],
#     "F": [("B", 2), ("D", 3)],
# }


# # Algo will start at specific node, then explore all possible paths from that node to find the shortest path to any of the other nodes
# def shortest_path(graph, start, target=""):
#     # track visited nodes - explore all nodes connected to start and calculate shortest path then remove start node and repeast process for closest neighbour etc.
#     unvisited_node = list(graph)
#     # track shortest distance to each node
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(
#         start
#     )  # returns in alphabetical order --> we want smallest distance (while loop param)
#     while unvisited_node:
#         current = min(
#             unvisited_node, key=distances.get
#         )  # define current node to visit *note pylance error but code words...don't want to use lambda function workaround for now just for typecheck
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 # keep track of node as distances dict updated (appended so is last item)
#                 if paths[node] and paths[node][-1] == node:
#                     # if shorter distance is found avoid assigning the same path to the node. (use copy of current path to avoid modifying original path list)
#                     paths[node] = paths[current][:]
#                 else:
#                     paths[node].extend(
#                         paths[current]
#                     )  # add the current node path to the neighbor node path
#                 paths[node].append(node)
#         unvisited_node.remove(current)

#     targets_to_print = [target] if target else graph
#     for node in targets_to_print:
#         if node == start:
#             continue  # skip start node
#         print(
#             f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}'
#         )
#     return distances, paths

#     print(f"Unvisited: {unvisited_node}\nDistances: {distances}\nPaths: {paths}")


# # for node in graph:
# # unvisited_node.append(node)
# # if node == start:
# #     distances[node] = 0
# # # initially all other nodes considered to be infinite distance from start node
# # else:
# #     distances[node] = float("inf")


# shortest_path(my_graph_weighted, "A")  # can add 3rd param to specify target node
# # >>> Unvisited: ['A', 'B', 'C', 'D']
# # Distances: {'A': 0, 'B': inf, 'C': inf, 'D': inf}
# # Paths: {'A': ['A'], 'B': [], 'C': [], 'D': []}
# # >>>
# # A-A distance: 0
# # Path: A
# # >>>
# # A-B distance: 3
# # Path: A -> B
# # >>>
# # A-C distance: 7
# # Path: A -> B -> C
# # >>>
# # A-D distance: 1
# # Path: A -> D


# # --------------------------------TUTORIAL 7---------------------------------------------------
# # Tutorial 7: Recursion - Tower of Hanoi Puzzle
# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1  # puzzle can be solved in 2^n - 1 moves
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}

# # Utility function for move() where eg. rod1 = source, rod2 = target for first if statement in move()
# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[rod2]:
#         forward = True
#     elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
#         rods[rod2].append(rods[rod1].pop())
#     else:
#         print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
#         rods[rod1].append(rods[rod2].pop())
#     print(rods)  # track progress
#     print("\n")


# # def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     # for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             # need to set a conditional for when number of disks is odd
#             if n % 2 != 0:
#                 print(f"Move {i + 1} allowed between {source} and {target}")
#                 make_allowed_move(source, target)
#             else:
#                 print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#                 make_allowed_move(source, auxiliary)
#         elif remainder == 2:
#             if n % 2 != 0:
#                 print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#                 make_allowed_move(source, auxiliary)
#             else:
#                 print(f"Move {i + 1} allowed between {source} and {target}")
#                 make_allowed_move(source, target)
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")
#             make_allowed_move(auxiliary, target)
#     # Recrusive Solution - see notes
#     # Does not use util function make_allowed_move() OR number_of_moves variable

# move(NUMBER_OF_DISKS, "A", "B", "C")

# A = list(range(NUMBER_OF_DISKS, 0, -1))
# B = []
# C = []
# # Recrusive Solution - see notes
#     # Does not use util function make_allowed_move() OR number_of_moves variable
# def move(n, source, auxiliary, target):
#     if n  <= 0:
#         return

#     #1 move n - 1 disks from source to auxiliary, so they are out of the way
#     move(n-1, source,  target, auxiliary)
#     #2 move the nth disk from source to target. remove last element from the rods[source] list and append it to the rods[target] list.
#     # rods[target].append(rods[source].pop())
#     target.append(source.pop())
#     # move the n - 1 disks that we left on auxiliary onto target
#     move(n-1,  auxiliary, source, target)
#     # display recursion progress
#     # print(rods, '\n')
#     print(A,B,C, '\n')
# # initiate call from source A to target C with auxiliary B
# print(NUMBER_OF_DISKS, A, B, C)

# # --------------------------------TUTORIAL 8---------------------------------------------------
# # Tutorial 8: Merge Sort Algo, (RECURSION) - Data Structures - see notes
# def merge_sort(array):
#     # BASE CASE: if array has 1 or 0 elements, it is already sorted
#     if len(array) <= 1:
#         return
#     # 1. Divide an unsorted sequence of items into sub-parts
#     middle_point = len(array) // 2
#     left_part = array[:middle_point]
#     right_part = array[middle_point:]
#     # 2. Sort the items in the sub-parts
#     merge_sort(left_part)
#     merge_sort(right_part)
#     # 3. Merge the sorted sub-parts
#     # variables will help keep track of each index during sorting process
#     left_array_index = 0
#     right_array_index = 0
#     sorted_index = 0
#     # COMPARE elements in left and right arrays and merge them in sorted order
#     while left_array_index < len(left_part) and right_array_index < len(right_part):
#         if left_part[left_array_index] < right_part[right_array_index]:
#             array[sorted_index] = left_part[left_array_index]
#             left_array_index += 1
#         else:
#             array[sorted_index] = right_part[right_array_index]
#             right_array_index += 1
#         sorted_index += 1
#         # another while loop to handle remaining elements in left and right arrays
#         while left_array_index < len(left_part):
#             array[sorted_index] = left_part[left_array_index]
#             left_array_index += 1
#             sorted_index += 1
#         while right_array_index < len(right_part):
#             array[sorted_index] = right_part[right_array_index]
#             right_array_index += 1
#             sorted_index += 1
# if __name__ == '__main__':
#     numbers = [4, 10, 6, 14, 2, 1, 8, 5]
#     print('Unsorted array: ')
#     print(numbers)
#     merge_sort(numbers)
#     print('Sorted array: ' + str(numbers))


# --------------------------------TUTORIAL 9---------------------------------------------------
# Tutorial 9: OOP - Sudoku puzzle
class Board:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        # string represents sudoku board in a visually appealing ASCII art style. It uses special Unicode characters to draw the borders and intersections.
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines
        for index, line in enumerate(self.board):
            # store elements of a single row of the board
            row_list = []
            # split each row in 3 sections to create 3x3 squares/grid
            # need to create 3 line segments to pass to enumerate() function - slice list
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                # join elements of 'part' with | char (use generator function)
                row_square = "|".join(str(item) for item in part)
                row_list.extend(row_square)
                # Check if current segment is NOT the last one
                if square_no != 3:
                    row_list.append("║")
            # create str representation of row with spaces between elements
            row = f'║ {" ".join(row_list)} ║\n'
            # when passing input '0' will be used for empty cells. For better UI change to ' '
            row_empty = row.replace("0", " ")
            board_string += row_empty
            # check if current row index is NOT the last one ( < index 8 )
            if index < 8:
                # check if row is the last row in the 3x3 square ( index % 3 == 2 ) index 2, 5, 8
                if index % 3 == 2:
                    board_string += (
                        f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                    )
                else:
                    board_string += middle_lines
            # handle when current row is last row of the board
            else:
                board_string += lower_lines
        return board_string

    # method to find empty cells in the board
    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                # try to find first occurence of 0 in the current row
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None  # if no empty cells are found i.e. board is filled

    # method to check if number can be inserted in a specific row
    def valid_in_row(self, row, num):
        # check num is not already in the row
        return num not in self.board[row]

    # method to check if number can be inserted in a specific col
    def valid_in_col(self, col, num):
        # check num is equal to a num in the col of the current row
        for row in range(9):
            # for each element in specified col of current row check value != num
            return all(self.board[row][col] != num for row in range(9))

    # method to check if number can be inserted in the 3x3 square
    def valid_in_square(self, row, col, num):
        # calculate starting row index for 3x3 block in board grid (each would be multiple of 3)
        row_start = (row // 3) * 3
        # calculate starting col index for 3x3 block in board grid (each would be multiple of 3)
        col_start = (col // 3) * 3

        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                # (prevent) check if specified number (num) already present in current cell of the 3x3 square
                if self.board[row_no][col_no] == num:
                    return False
        return True

    # method to check if num valid choice for an empty cell by validating its compatibility with the row, column, and 3x3 square of the specified empty cell. USES UTIL FUNCTION
    def is_valid(self, empty, num):
        # unpack the empty tuple into row and col
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)

        return all([valid_in_row, valid_in_col, valid_in_square])

    # method to solve sudoku in-place (modify existing board instead of creating new board)
    def solver(self):
        # check if there are any empty cells left on the board; if none then puzzle solved
        if (next_empty := self.find_empty_cell()) is None:
            return True
        else:  # still empty cells
            for guess in range(1, 10):
                # for each number (guess) check if the number is valid choice for current empty cell
                self.is_valid(next_empty, guess)
                # unpack the next_empty tuple into row and col
                row, col = next_empty
                # assign value of guess to the current empty cell since valid
                self.board[row][col] = guess
                # recursive call to solver() to continue solving the puzzle
                if self.solver():
                    return True
                else:
                    # if False then 'guess' led to an unsolvable sudoku --> so reset the cell to 0
                    self.board[row][col] = 0
            return False  # if no valid guess found for current empty cell


# --------------------------------------Board Class---------------------------------------------------------------


# function to print and solve the sudoku board
def solve_sudoku(board):
    gameboard = Board(board)
    print(f"\nPuzzle to solve:\n{gameboard}")
    if gameboard.solver():
        print("\nSolved puzzle:")
        # current state of the board using __str__method for Board class
        print(gameboard)
    else:
        print("\nThe provided puzzle is unsolvable.")
    return gameboard


puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5],
]

solve_sudoku(puzzle)
