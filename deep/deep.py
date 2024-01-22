print("What is the answer to the Great Question of Life, the Universe and Everything?")

name = input("")


match name:
    case "42":
        print("Yes")
    case "Forty Two":
        print("Yes")
    case "forty-two":
        print("Yes")
    case "forty two":
        print("Yes")
    case "FoRty TwO":
        print("Yes")
    case " 42 ":
        print("Yes")
    case _:
        print("No")
