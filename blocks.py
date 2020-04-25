name = input("please enter your name: ")
age = int(input("please enter your age: {0}? ".format(name)))
print(age)
#
# if age >=18:
#     print("you are old enough to vote")
# else:
#     print("Please come back in {0} years".format(18-age))
if age < 18:
    print("Please come back in {0} years".format(18-age))
elif age == 900:
    print("Sorry, You die in return of the Jedi")
else:
    print("you are old enough to vote")

