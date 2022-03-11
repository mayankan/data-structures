"""
    @Author: Mayank Anand
    @Date: 2022-03-10
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs
    """
import calendar


def main():
    month = int(input("Enter month in dd(20) format: "))
    year = int(input("Enter year in yyyy(2020) format: "))
    print(calendar.month(year, month))


if __name__ == "__main__":
    main()
