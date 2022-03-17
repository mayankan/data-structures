"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : Tuple Data Structure Programs - Creating a tuple
    """


def create_tuple():
    """
    Description:
        Creates tuple with different methods and prints them.
    Return:
        None
    """
    # creating an empty tuple
    sample_tuple = ()
    print(sample_tuple)
    # Create an empty tuple with tuple() built-in function
    sample_tuple = tuple()
    print(sample_tuple)
    # tuple with elements
    sample_tuple = (2, 4, 6, 8, 10)
    print(sample_tuple)


def main():
    try:
        create_tuple()
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
