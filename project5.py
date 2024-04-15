import copy
import random

# Probability Calculator
# Program to determine approx. prob of drawing certain balls randomly (from a Hat)


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    # Hat should take variable num of args that specify num of Balls of each colour in the hat.
    # contents should be a list of strings containing one item for each ball where item == color of ball
    # eg Hat(red=2, blue=1) --> contents = ['red', 'red', 'blue']

    # Method to RANDOMLY remove balls from contents (in Hat) and return those balls as a list of strings
    def draw(self, num_balls):
        if num_balls > len(self.contents):
            copied_list = self.contents.copy()
            self.contents.clear()
            return copied_list

        return [
            self.contents.pop(random.randrange(0, len(self.contents)))
            for _ in range(num_balls)
        ]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful_matches = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        # Check if the count of each color in drawn_balls is at least as high as expected
        if all(
            drawn_balls.count(color) >= num for color, num in expected_balls.items()
        ):
            num_successful_matches += 1
    return num_successful_matches / num_experiments


# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
#     # iterate over items in expected_balls dict. 'num' is value of current item in dict (# of balls of that color)
#     # use list comprehension to create new list by adding value of key to the list.
#     expected_num_of_balls = [num for color, num in expected_balls.items()]
#     num_successful_matches = 0

#     for _ in range(num_experiments):
#         hat_copy = copy.deepcopy(hat)
#         drawn_balls = hat_copy.draw(num_balls_drawn)
#         num_of_balls = [drawn_balls.count(color) for color in expected_balls]
#         num_successful_matches += 1 if num_of_balls >= expected_num_of_balls else 0

#     return num_successful_matches / num_experiments


# experiment function should return a probability of getting a specified num of expected_balls when you draw num_balls_drawn from the hat num_experiments times.
# Probability calculated as ('M' times you get expected_balls) / ('N' num_experiments)
