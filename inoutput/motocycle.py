import shelve

with shelve.open("C:/Users/user/Downloads/bike") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 dream"
    # bike["color"] = "red"
    # bike["engine_size"] = 250
    # for key in bike:
    #     print(key)
    # print("=" * 40)
    print(bike["engine_size"])
    print(bike["color"])