"""
    @Author: Mayank Anand
    @Date: 2022-03-19
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-19
    @Title: String Data Structure Programs - Add ing or ly as per string
    """
import logger

logger = logger.logging_init('suffix_ing_ly')


def add_ing_ly(given_string):
    """
    Description:
        Adds 'ing' to a string with more than 2 characters and adds 'ly' if it contains 'ing' already
    Parameter:
        given_string: Given string given by user.
    Return:
        String after adding suffix 'ly' and 'ing' if 'ing' is already present in given string.
    """
    str_len = len(given_string)
    if str_len >= 3 and given_string[-3:] == 'ing':
        given_string = given_string + 'ly'
    else:
        given_string = given_string + 'ing'
    return given_string


def main():
    try:
        sample_string = input("Enter a string : ")
        logger.info("String after adding suffix: {add_ing_ly(sample_string)}")
    except Exception as e:
        logger.error(f"{e} is raised")


if __name__ == "__main__":
    main()
