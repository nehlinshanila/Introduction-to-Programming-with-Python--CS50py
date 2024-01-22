def main():
    time = input("whats time: ")
    converted = convert(time)
    if converted >= 7 and converted <= 8:
        print("breakfast time")
    elif converted >= 12 and converted <= 13:
        print("lunch time")
    elif converted >= 18 and converted <= 19:
        print("dinner time")


def convert(time):
   hours, minutes = time.split(":")
   hours = float(hours) + (float(minutes) / 60)
   return hours

if __name__ == "__main__":
    main()
