low  = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Please press Enter to start a game ")
guesses = 1

while True:
    print("")
    guess = low + (high - low) // 2
    high_low = input("My guess is {}, Should I guess higher or Lower?" \
               "Enter l or h, or c if i was correct ".format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
        break
    else:
        print("Please Enter h,l or c")

    guesses = guesses + 1
