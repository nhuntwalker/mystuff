import random as rand
import numpy as np

colors = 'black','red','blue'
hat = []
for color in colors:
    for i in range(4):
        hat.append(color)

def draw_ball(hat):
    color = rand.choice(hat)
    hat.remove(color)
    return color, hat

