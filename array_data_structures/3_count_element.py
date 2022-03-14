"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Array Data Structure Programs - Count no of occurences of an element in an array
    """
import array


def check_occurrence(array_5_elements, occurrence_val):
    """
    Returns number of occurrences of an element in given array.
    Parameters:
        array_5_elements: Given array in which number of occurrences are to be counted.
        occurrence_val: Element which has to be counted.
    Return:
        Number of occurrences of the given element in the given array.
    """
    try:
        count = 0
        for occurrence in array_5_elements:
            if occurrence == occurrence_val:
                count += 1
        return count
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
        array_5_elements = array.array('i', [1, 3, 4, 3, 2, 5, 6, 4, 3, 2])
        print_array(array_5_elements)
        occurrence_val = int(input("Enter the element in the above array to check number of occurrences: "))
        no_of_occurrences = check_occurrence(array_5_elements, occurrence_val)
        print("No. of occurrences in array are {}".format(no_of_occurrences))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
