import shelve
books = shelve.open("C:/Users/user/Downloads/book")

books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled_eggs" : ["eggs", "butter","meals"],
                    "soup":["tin of soup"],
                    "pasta":["pasta", "cheese"]}
books["maintenance"] ={"stock": ["oil"],
                       "loose": ["gaffer tape"]}

print(books["recipes"]["soup"])
print(books["maintenance"]["loose"])
for i in books["recipes"]:
    dic_key = books["recipes"][i]
    print(i, dic_key)

books.close()