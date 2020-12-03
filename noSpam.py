menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ]

# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item)
#     print("\n")

for meal in menu:
    long_man = len(meal) - 1
    for index, item in enumerate(reversed(meal)):
        if item == "spam":
            del meal[long_man - index]

for meal in menu:
    print(meal)
