"""
    @Author: Mayank Anand
    @Date: 2022-03-19
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-19
    @Title: String Data Structure Programs - Reverse string
    """
import logger

logger = logger.logging_init('reverse_string')


def string_reverse(given_string):
    """
    Description:
        Reverses the given string.
    Parameter:
        given_string: Given string that is to be reversed.
    Return:
        Reversed string.
    """
    return given_string[::-1]


def main():
    try:
        input_string = input("Enter a string : ")
        logger.info(f"Reversed String : {string_reverse(input_string)}")
    except Exception as e:
        logger.error(f"{e} is raised")


if __name__ == "__main__":
    main()
