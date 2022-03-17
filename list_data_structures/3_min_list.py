"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-16
    @Title : List Data Structure Programs - Calculates the Smallest number from list
    """
import logging


def min_element(given_list):
    """
    Description :
        Calculates minimum value in given list.
    Parameters :
        given_list: The list in which minimum value is to be fetched.
    Return:
         Element with the smallest value in the given list.
    """
    try:
        given_list.sort()
        return given_list[:1]
        # Method 2
        # return min(given_list)
    except Exception as e:
        logging.exception("{} is raised".format(e))


def main():
    try:
        logging.info("Main function of Smallest element in list program started successfully.")
        list1 = [3, 5, 7, 9, 11, 13, 15, 17, 19]
        print("List:", list1)
        print("Smallest value of all elements in List:", min_element(list1))
        logging.info("Main function of Smallest element in list program completed successfully.")
    except Exception as e:
        logging.exception("{} is raised".format(e))


if __name__ == "__main__":
    main()
