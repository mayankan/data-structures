"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Array Data Structure Programs - Reverse elements of an array
    """
import array


def reverse_array_slicing(array_5_elements):
    """
    Description:
        Reverses array using slicing technique
    Parameter:
        array_5_elements: Array to be reversed.
    Return:
        Reversed array
    """
    try:
        array_5_elements = array_5_elements[::-1]
        return array_5_elements
    except Exception as e:
        print("{} is raised.".format(e))


def reverse_array(array_5_elements):
    """
    Description:
        Reverses array using array reverse method.
    Parameter:
        array_5_elements: Array to be reversed.
    Return:
        Reversed array
    """
    try:
        array_5_elements.reverse()
        return array_5_elements
    except Exception as e:
        print("{} is raised.".format(e))


def print_array(array_5_elements):
    """
    Description:
        Prints each element in the given array.
    Parameter:
        array_5_elements: Array with 5 elements to print each element.
    Return:
        None
    """
    try:
        for index in range(len(array_5_elements)):
            print(index + 1, "Index value is:", array_5_elements[index])
    except Exception as e:
        print("{} is raised.".format(e))


def main():
    try:
        array_5_elements = array.array('i', [1, 3, 4, 2, 5])
        reverse_array(array_5_elements)
        print("Reversed array is: ")
        print_array(array_5_elements)
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
