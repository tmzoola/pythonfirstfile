name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age <= 31:
    print("welcome, {} to the holiday".format(name))
else:
    print("Sorry you can not participate")
