#Write your code below this line
def paint_calc(height, width, cover):
    fun = test_h * test_w // coverage
    
    print(f"You'll need {fun} cans of paints")

#Write your code above this line

#Don't change the code below
test_h = int(float(input("Height of wall: ")))
test_w = int(input("width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)