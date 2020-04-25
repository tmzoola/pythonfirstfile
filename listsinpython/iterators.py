strings = ["1","2","3","4","5","6"]
my_iterator = iter(strings)

for i in range(0, len(strings)):
    next_item = next(my_iterator)
    print(next_item)
