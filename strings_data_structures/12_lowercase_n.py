"""
    @Author: Mayank Anand
    @Date: 2022-03-19
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-19
    @Title: String Data Structure Programs - Lowercase n characters in String
    """
import logger

logger = logger.logging_init('lowercase_n')


def lower_first_char(given_string, no_of_char):
    """
    Description:
        Converts the first n characters of string into lower case.
    Parameters:
        given_string: Given string whose first n characters are to be converted into lower case.
        no_of_char: Number of characters in the given string to be converted into lower case.
    Return:
        Given String with first n number of characters converted to lower case.
    """
    return given_string[:no_of_char].lower() + given_string[no_of_char:]


def main():
    try:
        input_string = input("Enter a string: ")
        no_of_char = int(input("Enter the first n characters that is to be shifted to lowercase: "))
        logger.info(f"String after conversion: {lower_first_char(input_string, no_of_char)}")
    except Exception as e:
        logger.error(f"{e} is raised")


if __name__ == "__main__":
    main()
