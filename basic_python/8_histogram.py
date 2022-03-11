"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs
    """
import matplotlib.pyplot as plt


def main():
    try:
        no_of_values = int(input("Enter number of values to input to create a histogram: "))
        list_nos = []
        for no in range(no_of_values):
            list_nos.append(int(input("Enter {} value: ".format(no + 1))))
        plt.hist(list_nos)
        plt.show()
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
