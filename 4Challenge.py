starters = "Squirtle", "Totodile", "mudkip", "Piplup", "Oshawott", "Froakie", "Popplio", "Sobble", "Another type"

response = 0

while response != 9:
    print("Pick an option:")
    for num in range(len(starters)):
        print(f"{num + 1}. {starters[num]}")

    response = int(input())

    if 0 < response < 9:
        print(f"Good choice, {starters[response - 1]} is a fine Pokemon\n")
    elif response == 9:
        break
    else:
        print("Come on, pick one of the options!\n")

print("Why would you pick another type?")