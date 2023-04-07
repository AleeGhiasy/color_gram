
import colorgram
#   receiving color objects from the img.jpeg through the colorgram module
colors = colorgram.extract("img.jpeg",30)
dots = []


def pick_hsl():
    """this function is made to cover the below code from not running since we dont need. but I still kept it for
    learning purpose"""
    for color in colors:
        # using the color object to access hue, lightness, and saturation of each color objects
        hue = color.hsl.h
        light= color.hsl.l
        sat = color.hsl.s
        new_color = (hue,light,sat)
        dots.append(new_color)

    print(dots)


# copying the colors from dots
color_range = [(39, 158, 205), (240, 102, 237), (35, 104, 223), (13, 108, 219), (236, 142, 200), (142, 163, 146), (22, 159, 154), (146, 97, 184), (105, 110, 174), (167, 93, 203), (161, 39, 171), (231, 173, 120), (40, 120, 240), (229, 116, 182), (133, 112, 225), (233, 198, 143), (109, 157, 82), (105, 28, 183), (102, 86, 136), (132, 180, 176), (242, 35, 167), (10, 37, 206), (178, 150, 145), (117, 181, 120), (2, 93, 233), (6, 133, 208)]
import random
import turtle as tim
tim.hideturtle()
tim.penup()
tim.colormode(255)
#   initial positioning of our pointer
tim.setheading(135)
tim.forward(310)
tim.setheading(0)
# drawing our dots
number_of_dots = 100
for dot in range(1,number_of_dots+1):
    print(tim.dot(20,random.choice(color_range)))
    tim.forward(50)
    if dot % 10 == 0:
        tim.setheading(-90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)