from turtle import Turtle, Screen
import random

tim = Turtle()

colours = ["red", "blue", "gold", "khaki3", "magenta", "orange", "purple", "tan4"]

n = 4
for _ in range(7):
    print(f"Value of before small loop {n}")
    tim.color(random.choice(colours))
    for _ in range(n):
        tim.forward(100)
        tim.right(360/n)
    n += 1
    print(f"Value of after small loop {n}")
