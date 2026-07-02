#Write your code below this line
import math


def paint_calc(height, width, cover):
    area = height * width
    cans = math.ceil(area / cover)
    print(f"You'll need {cans} cans of paint.")


test_h = float(input("Height of wall: "))
test_w = float(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)
