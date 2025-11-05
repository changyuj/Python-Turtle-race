from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=700)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(2,2,1)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-380,y=(turtle_index*70)-160)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        rand_distance = random.randint(0, 20)
        turtle.speed("fastest")
        turtle.forward(rand_distance)
        if turtle.xcor() > 350:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winder!")
            else:
                print(f"You lost! The {winning_color} turtle is the winder!")
            

screen.exitonclick()