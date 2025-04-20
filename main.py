import turtle
import pandas as pd
import time

FONT = ("Times New Roman",8,'normal')

screen = turtle.Screen()
screen.title("Name The US States")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

runtime = 60 * 10 #60 secs * 10 for 10 minutes
close_time = time.time() + runtime

with open("50_states.csv") as state_data:
    data = pd.read_csv(state_data)

state_names = data.state.to_list()

#x_michigan = data[data.state == "Michigan"].x
#print(x_michigan)

game_on = True
correct = 0
guessed_states = []

while game_on:
    user_answer = screen.textinput(title=f"{correct}/50 Correct | Guess the next state",prompt="What's another state name?")
    
    if user_answer is None or user_answer.lower() == "exit":
        #If user clicks cancel or types exit, the game will end and the screen will close
        game_on = False
        screen.bye()
        break
    
    for state in state_names:
        if (user_answer.lower() not in guessed_states) and (user_answer.lower() == state.lower()):
            correct += 1
            guessed_states.append(state.lower())
            x_cor = int(data[data.state == user_answer.title()].x)
            y_cor = int(data[data.state == user_answer.title()].y)
            t.goto(x_cor,y_cor)
            t.write(arg= f"{user_answer.title()}",font=FONT,align="center")

    #Chkecking if user guessed all 50 states
    if correct == 50:
        game_on = False
        screen.bye()

    #Checking if the timer ran out
    if time.time() >= close_time:
        game_on = False
        screen.bye()

states_not_guessed = []

for state in state_names:
    if state.lower() not in guessed_states:
        states_not_guessed.append(state)

not_guessed = pd.DataFrame(states_not_guessed)
not_guessed.to_csv("Not_Guessed.csv")

print(f"You missed the following states:")

print(not_guessed)

print(f"\n\nThanks for playing the game. Final score = {correct}/50.\n")