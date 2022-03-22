"""
    @Author: Mayank Anand
    @Date: 2022-03-19
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-19
    @Title : String Data Structure Programs - Unique sorted words in List
    """
import logger

logger = logger.logging_init('unique_sorted_list')


def unique_sorted_list(given_str_list):
    """
    Description:
        Gets unique words from given list and sorts them.
    Parameters:
        given_str_list: Given list of words separated by comma.
    Return:
        List of unique words sorted alphanumerically converted to string.
    """
    str_list = given_str_list.split(", ")
    str_set = set(str_list)
    return_list = list(str_set)
    return_list.sort()
    return_string = ", ".join(return_list)
    return return_string


def main():
    try:
        input_string = input("Enter a comma separated string of words: ")
        logger.info("Unique words in list sorted alphanumerically:", unique_sorted_list(input_string))
    except Exception as e:
        logger.error("{} is raised".format(e))


if __name__ == "__main__":
    main()
