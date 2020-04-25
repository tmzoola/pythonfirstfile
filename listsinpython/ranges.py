# my_list = list(range(10))
# print(my_list)
#
# even = list(range(0,10,2))
# odd = list(range(1,10,2))
#
# print(even)
# print(odd)
#
sevens = range(7,1000000,7)

while True:
    x = int(input("Please enter a positive number less than one million: "))
    if x in sevens:
        print("{} is divisible by 7".format(x))
        break
    else:
        print("This is not divisible by 7, try again")
