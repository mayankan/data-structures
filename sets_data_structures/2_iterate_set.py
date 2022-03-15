"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Sets Data Structure Programs - Iterate a set
    """


def iterate_set(set1):
    """
    Description:
        Iterates each member of set and prints it.
    Parameter:
        set1: set to be iterated.
    Return:
        None
    """
    for value in set1:
        print(value)


def main():
    set1 = {3, 5, 7, 9}
    iterate_set(set1)


if __name__ == "__main__":
    main()
