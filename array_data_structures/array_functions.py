"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Array Data Structure Programs - All functions of an array
    """
import array


def insert_at_last(array_5_elements, element_add):
    """
    Description:
        Adds the given element at the last position in the given array.
    Parameters:
        array_5_elements: Given array in which given element is appended.
        element_add: Element to be added in the given array.
    Return:
        Array after appending the given element.
    """
    try:
        array_5_elements.append(element_add)
        return array_5_elements
    except Exception as e:
        print("{} is raised.".format(e))


def insert_array(array_5_elements, element_add, pos):
    """
    Description:
        Adds the given element at the given position in the given array.
    Parameters:
        array_5_elements: Given array in which given element is added at the given position.
        element_add: Element to be added in the given array.
        pos: Position where element is to be added.
    Return:
        Array after adding the given element at the given position.
    """
    try:
        array_5_elements.insert(pos-1, element_add)
        return array_5_elements
    except Exception as e:
        print("{} is raised.".format(e))


def remove_at_position(array_5_elements, pos):
    """
    Description:
        Removes the given element at the given position in the given array.
    Parameters:
        array_5_elements: Given array in which given element is removed at the given position.
        pos: Position where element is to be removed.
    Return:
        Array after removing the given element at the given position
    """
    try:
        array_5_elements.pop(pos-1)
        return array_5_elements
    except Exception as e:
        print("{} is raised.".format(e))


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


def index_element(array_5_elements, element):
    """
    Description:
        Returns index of given element from the given array.
    Parameters:
        array_5_elements: Given array in which index of given element is to be fetched.
        element: Element of which index is to be fetched.
    Return:
        Index of given element in the given array.
    """
    try:
        index_of_element = array_5_elements.index(element)
        return index_of_element
    except Exception as e:
        print("{} is raised.".format(e))


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
