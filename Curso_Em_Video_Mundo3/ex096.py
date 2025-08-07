#CHALLENGE 96: Area of rectangle
#GOAL:Write code that creates a function to calculate the are of a rectangle baseed in its height and width
#SKILL: Learning about functions pt1

def area(h, w):
    print(f'The area of the rectangle {h}x{w} is {h*w:.2f}m²')


area(float(input('Height (m): ')), float(input('Width (m): ')))