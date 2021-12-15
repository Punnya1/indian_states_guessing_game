import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian_States_Game")
image = "indian_blank_states.gif"
screen.addshape(image)
screen.setup(1200, 900)
turtle.shape(image)
score = 0
guessed_list = []
state_info = pandas.read_csv("29_states.csv")
states_list = state_info["state"].to_list()
while score < 29:
    answer_state = screen.textinput(title=f"{score}/29 States Correct", prompt="What is another state's name.").title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_list]
        new_states = pandas.DataFrame(missing_states)
        new_states.to_csv("states_to_learn")
        break

    if answer_state in states_list:
        if answer_state not in guessed_list:
            guessed_list.append(answer_state)
            score += 1
            tim = turtle.Turtle()
            tim.hideturtle()
            tim.penup()
            state_data = state_info[state_info.state == answer_state]
            tim.goto(int(state_data["x"]), int(state_data["y"]))
            tim.write(answer_state)
