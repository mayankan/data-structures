from datetime import datetime


def main():
    date_1 = datetime.strptime(input("Enter first date in dd/mm/yyyy(20/02/2020) format: "), "%d/%m/%Y")
    date_2 = datetime.strptime(input("Enter second date in dd/mm/yyyy(20/02/2020) format: "), "%d/%m/%Y")
    diff = date_2 - date_1
    print(diff.days, "days")


if __name__ == "__main__":
    main()
