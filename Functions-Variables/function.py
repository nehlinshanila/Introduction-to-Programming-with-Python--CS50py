# def hello(to):
#     # name is to inside this function
#     print("Hello", to)
#     # make sure to go ahead 4 spaces

# name = input("What's your name? ")
# hello(name)
# # calling hello and passing as input the name variable as an argument


# main fucntion at top
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    # name is to inside this function
    print("Hello, ", to)
    # make sure to go ahead 4 spaces


main()
# calling main function else nothing will work