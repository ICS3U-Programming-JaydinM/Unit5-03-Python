#!/usr/bin/env python3

# Made by Jaydin Madore
# Made on 2022-11-30
# This program calculates the middle mark of a level


# Defining middle mark function
def Mark(level):

    # Match case statement structure used for each possible level value
    match level:
        case "4+":
            return "97.5%"
        case "4":
            return "90.5%"
        case "4-":
            return "83%"
        case "3+":
            return "78%"
        case "3":
            return "74%"
        case "3-":
            return "71%"
        case "2+":
            return "68%"
        case "2":
            return "64.5%"
        case "2-":
            return "61%"
        case "1+":
            return "58%"
        case "1":
            return "54.5%"
        case "1-":
            return "51%"
        case "R":
            return "24.5%"
        case _:
            return "invalid input"


def main():
    # Gets the user's grade
    user_level = input("What is your grade: ")

    # Call the function to convert the user level to a percentage
    user_mark = Mark(user_level)

    # Checks for invalid input
    if user_mark == -1:
        print("Please input a valid grade")


    # Displays the middle mark to the user
    else:
        print("{} has a middle percentage of {}".format(user_level, user_mark))


if __name__ == "__main__":
    main()
