"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : Tuple Data Structure Programs - Reversing tuple
    """


def reverse_tuple(given_tuple):
    """
    Description :
        Reverse the given tuple.
    Parameters :
        given_tuple: Given tuple which is to be reversed.
    Return:
        Reversed tuple.
    """
    result_tuple = given_tuple[::-1]
    return result_tuple


def main():
    sample_tuple = ("Mayank", 3.17, 22, True)
    print("Given tuple:", sample_tuple)
    print("Tuple after reversing items:", reverse_tuple(sample_tuple))


if __name__ == "__main__":
    main()
