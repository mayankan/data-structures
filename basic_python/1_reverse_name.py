"""
    @Author: Mayank Anand
    @Date: 2022-03-10
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs - Reverse First Name & Last Name
    """


def reverse_name(_f_name, _l_name):
    """
    Description:
        Returns last name and first name separated by space.
    Parameters:
        _f_name: First name input by user.
        _l_name: Last name input by user.
    Return:
        string having last name and first name separated by space.
    """
    try:
        return _l_name + " " + _f_name
    except Exception as e:
        print("{} is raised.".format(e))


def main():
    try:
        f_name = input("Enter your first name: ")
        l_name = input("Enter your last name: ")
        print("Printing Last Name and First Name:")
        print(reverse_name(f_name, l_name))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
