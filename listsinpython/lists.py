menu = []
menu.append(["egg","spam","bacon"])
menu.append(["egg","sausage","bacon"])
menu.append(["egg","spam",])
menu.append(["egg","bacon","spam"])
menu.append(["egg","bacon","sausage","spam"])
menu.append(["spam","bacon","sausage","spam"])
menu.append(["egg","spam","bacon","spam","spam"])
menu.append(["spam","egg","sausage","spam"])

for meal in menu:
    if not "spam" in meal:
        print(meal)
for meals in menu:
    print(meals)
    for ingred in meals:
        print(ingred)