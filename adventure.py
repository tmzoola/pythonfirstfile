available_exit = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exit:
    chosen_exit = input("please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break
else:
    print("Aren't you glad you got out of there")
