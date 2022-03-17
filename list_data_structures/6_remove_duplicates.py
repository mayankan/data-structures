"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : List Data Structure Programs - Remove duplicate elements from list
    """
import logging


def remove_duplicates(given_list):
    """
    Description:
        Removes duplicates from given list in parameter.
    Parameter:
        given_list: Given list to remove duplicate elements.
    Return:
        List after removing duplicates.
    """
    result_list = []
    for element in given_list:
        if element not in result_list:
            result_list.append(element)
    return result_list


def main():
    try:
        sample_list = [3, 5, 7, 9, 11, 13, 14, 14, 15, 17, 19, 19]
        print("List:",sample_list)
        print("List after removing duplicates:", remove_duplicates(sample_list))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
