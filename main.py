from turtle import Turtle, Screen
import pandas



data = pandas.read_csv("50_states.csv")
name_of_state = data["state"]



screen = Screen()
screen.setup(800, 800)


screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle(image)




moving_name = Turtle()
moving_name.penup()
moving_name.hideturtle()


game_is_on = True
score = 0
state_correct = []

while game_is_on:
    user_guess = screen.textinput(f"your score is {score}/50", "name of states: ").title()

    if user_guess == "Exit":
        missing_state =[state for state in name_of_state if state not in state_correct]
        # missing_state = []
        # for state in name_of_state:
        #     if state not in state_correct:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state.csv")
        break
    for name in name_of_state:
        if user_guess == name:
            row_info = data[name_of_state == user_guess]
            moving_name.goto(int(row_info["x"]), int(row_info["y"]))
            moving_name.write(f"{user_guess}", move=True, align="center")
            score = score + 1
            state_correct.append(user_guess)





if score == 50:
    game_is_on = False
    print("You Win")



