"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : Tuple Data Structure Programs - Creating a tuple with multiple data types
    """


def create_tuple_datatypes():
    """
    Description:
        Creates tuple with multiple data types.
    Return:
        Tuple with multiple data types.
    """
    # Creating a tuple with different data types
    sample_tuple = ("Mayank", 3.17, 22, True)
    return sample_tuple


def main():
    try:
        print(create_tuple_datatypes())
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
