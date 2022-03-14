"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Array Data Structure Programs - Remove first instance of an element from an array.
    """
import array


def remove_element_array(array_5_elements, element_remove):
    """
    Description:
        Removes the first instance of given element from the given array.
    Parameters:
        array_5_elements: Given array in which first instance of given element is removed.
        element_remove: Element which has to be removed from given array
    Return:
        Array after removing the first instance of the given element.
    """
    try:
        array_5_elements.remove(element_remove)
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
        array_5_elements = array.array('i', [1, 3, 4, 3, 2, 5])
        print_array(array_5_elements)
        element_remove = int(input("Enter the element in the above array to be removed: "))
        remove_element_array(array_5_elements, element_remove)
        print("Array after removal of given element is: ")
        print_array(array_5_elements)
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
