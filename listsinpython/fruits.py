fruit = {"orange": "sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
print(fruit)

veg = {"carbage": "every child's favorite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can i have some more fruit, please"}
print(veg)

veg.update(fruit)

print(veg)