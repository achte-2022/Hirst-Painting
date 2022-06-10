#Importing Libraries
import turtle
import colorgram
import random

#Constants
MAX_INTENSITY = 255
NUM_COLORS = 50
PAINTING = 'images/painting.jpg'
WINDOW_HEIGHT = 330
WINDOW_WIDTH = 330
SPEED = 'fastest'
BG_COLOR = 'black'
DOT_SIZE = 20
NUM_COLS = 10
NUM_ROWS = 10

#Turtle Color Setup    
turtle.colormode(MAX_INTENSITY)

#Extract Colors from .jpg file
def extract_colors(painting, num_colors):
    colors = colorgram.extract(painting, num_colors)
    colors_list = []
    for color in colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        rgb = (red, green, blue)
        colors_list.append(rgb)
    return colors_list


colors_list = extract_colors(PAINTING, NUM_COLORS)

#Function to create a Damien Hirst Spot Painting
def hirst_paint(turtle_object, start_x, start_y, num_rows, num_cols, circle_size, spacing):
    turtle_object.penup()
    turtle_object.goto(start_x, start_y)
    for i in range(num_rows):
        for j in range(num_cols):
            color = random.choice(colors_list)
            turtle_object.dot(circle_size, color)
            turtle_object.forward(spacing)
        turtle_object.goto(start_x , start_y + spacing * (i + 1))
    return

#Object Setup
window = turtle.Screen()
window.setup(WINDOW_HEIGHT, WINDOW_WIDTH)
window.bgcolor(BG_COLOR)
turtle_object = turtle.Turtle()
turtle_object.speed(SPEED)

spacing = DOT_SIZE + 10
start_x = -(WINDOW_HEIGHT / 2) + spacing
start_y = -(WINDOW_WIDTH / 2) + spacing

hirst_paint(turtle_object, start_x, start_y, NUM_ROWS, NUM_COLS, DOT_SIZE, spacing)
window.exitonclick()
