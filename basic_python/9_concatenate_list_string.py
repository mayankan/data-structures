"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs - Concatenate elements in list to single string
    """


def concatenate_string(list_vals):
    """
    Description:
        Returns string after concatenation of elements from given list.
    Parameter:
        list_vals: List of values to be concatenated.
    Return:
        String after concatenation of elements from list.
    """
    try:
        concat_value = ""
        for no in list_vals:
            concat_value += no
        return concat_value
    except Exception as e:
        print("{} is raised.".format(e))


def main():
    try:
        no_of_values = int(input("Enter number of values to input in list: "))
        list_vals = []
        for no in range(no_of_values):
            input_str = str(input("Enter {} value: ".format(no + 1)))
            list_vals.append(input_str)
        print("The concatenated string is:", concatenate_string(list_vals))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
