"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs - Print Histogram using given integers
    """
import matplotlib.pyplot as plt


def input_vals(no_of_values):
    """
    Description:
        Returns input values in list for the given number of inputs.
    Parameters:
        no_of_values: number of values to add into a list
    Returns:
        Integer Input values in list given by the user
    """
    list_nos = []
    for no in range(no_of_values):
        list_nos.append(int(input("Enter {} value: ".format(no + 1))))
    return list_nos


def main():
    try:
        no_of_values = int(input("Enter number of values to input to create a histogram: "))
        # Using function to get values in list
        list_nos = input_vals(no_of_values)
        # Histogram Plotting Function
        plt.hist(list_nos)
        plt.show()
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
