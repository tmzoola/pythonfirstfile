import shelve

# with shelve.open("C:/Users/user/Downloads/ShelfTest") as fruit:
fruit = shelve.open("C:/Users/user/Downloads/ShelfTest")
# fruit['orange'] = "a sweet, orange citrus fruit"
# fruit['apple'] = "a good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing bunches"
# fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])

# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + " - " + fruit[f])
#
# fruit.close()
for v in fruit.values():
    print(v)
print(fruit.values())
for f in fruit.items():
    print(f)
print(fruit.values())






