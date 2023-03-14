# This code will not work in repl.it as there is no access to the colorgram package here.###
# We talk about this in the video tutorials
import colorgram
import turtle
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

# print(rgb_colors)

# Color list from the image.png file
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]


def r_choice():
    return random.choice(color_list)


def hirst_paint():
    carlos.penup()
    y_position = -150
    for y in range(10):
        carlos.goto(-150, y_position)
        y_position += 40
        for x in range(10):
            carlos.dot(20, r_choice())
            carlos.fd(40)


carlos = turtle.Turtle()
screen = turtle.Screen()
carlos.hideturtle()
screen.colormode(255)
hirst_paint()
screen.exitonclick()
