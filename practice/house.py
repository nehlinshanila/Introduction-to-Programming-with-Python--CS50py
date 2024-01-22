name = input("whats your name: ")

# if name == "harry":
#     print("griffy")
# elif name == "marry":
#     print("priffy")
# else:
#     print("triffy")

match name:
    case "harry":
        print("griffy")
    case "marry":
        print("priffy")
    case "dfebhuias":
        print("triffy")
    case _:
        print("who")
