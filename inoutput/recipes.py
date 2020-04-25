import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter","meals"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('C:/Users/user/Downloads/Recipes', writeback=True) as recipe:
    # recipe["blt"] = blt
    # recipe["beans on toast"] = beans_on_toast
    # recipe["scrambled eggs"] = scrambled_eggs
    # recipe["pasta"] = pasta
    # recipe["soap"] = soup
    # temp_list = recipe["blt"]
    # temp_list.append("butter")
    # recipe["blt"] = temp_list
    #
    # temp_list = recipe["pasta"]
    # temp_list.append("tomato")
    # recipe["pasta"] = temp_list
    # recipe["soap"].append("croutons")

    for snack in recipe:
        print(snack, recipe[snack])

