
# x = 1
# y = 2
# z = x + y
# print(z)


# x = input("whats x?")
# y = input("whats y?")
# # z = x + y
# #  + here is used differently in strings
# # so we gonna use int(x) and int(y)
# z = int(x) + int(y)
# print(z)


#? nesting function
# x = int(input("whats x? "))
# y = int(input("whats y? "))
# print(x+y)


#? Float
# x = float(input("whats x? "))
# y = float(input("whats y? "))
# print(x+y)

#? Round
# x = float(input("whats x? "))
# y = float(input("whats y? "))
# z= round(x+y)
# print(z)

#? Round to nearest given digit method 1
# x = float(input("whats x? "))
# y = float(input("whats y? "))
# z= round(x/y, 2)
# print(z)

#? Round to nearest given digit method 2
# x = float(input("whats x? "))
# y = float(input("whats y? "))
# z= x+y
# print(f"{z:.2f}")

#? Comma
# x = float(input("whats x? "))
# y = float(input("whats y? "))
# z= round(x+y)
# print(f"{z:,}")

#? division
# x = float(input("whats x? "))
# y = float(input("whats y? "))
# z= round(x+y, 2)
# print(f"{z:.2f}")


#? Square of a value
# def main():
#     x = int(input("whats x? "))
#     print("x squared if", square(x))

# def square(n):
#     return n * n

# main()

#? Raise n to the power of 2
def main():
    x = int(input("whats x? "))
    print("x squared if", square(x))

def square(n):
    # return n ** n
    return pow(n, 2)

main()