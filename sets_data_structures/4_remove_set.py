"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Sets Data Structure Programs - Remove member(s) in set
    """


def remove_member(set1):
    """
    Description:
        Takes input from user for member(s) to be removed in the given set.
    Parameter:
        set1: Set with values in which member(s) are to be removed.
    Return:
        Set with removed members given by the user.
    """
    try:
        input_vals = int(input("Enter number of values to remove in set: "))
        for val in range(input_vals):
            input_val = int(input("Input {} value: ".format(val + 1)))
            set1.remove(input_val)
        return set1
    except Exception as e:
        print("{} is raised".format(e))


def main():
    try:
        set1 = {3, 5, 7, 9, 11, 13, 15, 17, 19}
        print("Set: ", set1)
        set1 = remove_member(set1)
        print("Set after removing member(s):", set1)
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
