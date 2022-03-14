"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Array Data Structure Programs - Prints each element in array
    """
import array


def print_array(array_5_elements):
    """
    Description:
        Prints each element in the given array.
    Parameter:
        array_5_elements: Array with 5 elements to print each element.
    Return:
        None
    """
    for index in range(len(array_5_elements)):
        print(index + 1, "Index value is:", array_5_elements[index])


def main():
    try:
        # Creating an array using array function
        array_5_elements = array.array('i', [1, 3, 4, 2, 5])
        print_array(array_5_elements)
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
