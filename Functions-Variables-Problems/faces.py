def main():
    write = input(" ")
    print(convert(write))

def convert(write):
    write = write.replace(":)", "🙂").replace(":(", "🙁")
    return write



main()


