import calendar


def main():
    month = int(input("Enter month in dd(20) format: "))
    year = int(input("Enter year in yyyy(2020) format: "))
    print(calendar.month(year, month))


if __name__ == "__main__":
    main()
