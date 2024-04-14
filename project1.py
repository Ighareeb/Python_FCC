# Arithmetic Formatter
# function receives list of strings == problems. Need to return problems arranged vertically and side-by-side.
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first = []
    second = []
    lines = []
    sumx = []
    # str_len = []

    # CHECK FOR INPUT ARGUMENT ERRORS
    for problem in problems:
        prob = problem.split()  # default delimiter is whitespace
        if prob[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        elif not (prob[0].isdigit() and prob[2].isdigit()):
            return "Error: Numbers must only contain digits."
        elif len(prob[0]) > 4 or len(prob[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        sum = ""
        if prob[1] == "+":
            sum = str(int(prob[0]) + int(prob[2]))
        else:
            sum = str(int(prob[0]) - int(prob[2]))
        # calculate length of longest operand. +2 ensures enough space for (operand +1 space +2 operator (+/-))
        length = max(len(prob[0]), len(prob[2])) + 2
        # str_len.append(length)
        first.append(prob[0].rjust(length))
        second.append(prob[1] + " " + prob[2].rjust(length - 2))
        lines.append("-" * length)
        sumx.append(sum.rjust(length))

        # join all the strings in each list into a single str with 4 spaces between each item
    first_line = "    ".join(first)
    second_line = "    ".join(second)
    line = "    ".join(lines)
    if show_answers:
        sum_line = "    ".join(sumx)
        # this is final formatting arrangement for the arithmetic problems
        arranged_problems = (
            first_line + "\n" + second_line + "\n" + line + "\n" + sum_line
        )
    else:
        arranged_problems = first_line + "\n" + second_line + "\n" + line
    return arranged_problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
