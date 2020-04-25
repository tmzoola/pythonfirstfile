import random

highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: Remove after guessing

print("Please guess the number between 1 and {}: ".format(highest))

guess = 0
while guess != answer:
    guess = int(input())
    if guess == answer:
        print("well done my brother")
        print("welcome to github skjdskdopskdposkd")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")





