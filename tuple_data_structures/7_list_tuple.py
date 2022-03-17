"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : Tuple Data Structure Programs - Creating a tuple using list
    """


def list_to_tuple(given_list):
    """
    Description:
        Creates tuple from given list.
    Parameter:
        given_list: Given list to be converted to tuple.
    Return:
        Tuple converted from given list.
    """
    return tuple(given_list)

def main():
    sample_list = ["apple", "banana", "cherry", "pie"]
    print("Given list:", sample_list)
    print("Tuple created from given list is:", list_to_tuple(sample_list))


if __name__ == "__main__":
    main()
