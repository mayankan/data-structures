"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : Tuple Data Structure Programs - Unpack tuple
    """


def unpack_tuple(given_tuple):
    """
    Description:
        Unpacks given tuple using ,(comma).
    Parameter:
        given_tuple: Given tuple to unpack multiple values in it.
    Return:
        three different values after unpacking given tuple.
    """
    element1, element2, element3 = given_tuple  # unpacking of a tuple
    return element1, element2, element3


def main():
    try:
        sample_tuple = (1.2, 3.4, 7.5)
        print("Sum of Tuple using unpacking method:", sum(unpack_tuple(sample_tuple)))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
