def leap_year():
    year = int(input("Please input a year: "))
    if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
        print("That's a leap year")
    else:
        print("That's not a leap year.")


if __name__ == '__main__':
    leap_year()