"""
    @Author: Mayank Anand
    @Date: 2022-03-19
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-19
    @Title: String Data Structure Programs - String in Upper and Lower cases.
    """
import logger

logger = logger.logging_init('upper_lowercase')


def string_upper_lower(given_string):
    """
    Description:
        Returns the given string in uppercase and lowercase.
    Parameter:
        given_string: Given string which changed to upper and lower cases.
    Return:
        Output string in upper and lower cases.
    """
    return given_string.upper(), given_string.lower()


def main():
    try:
        sample_string = input("Enter a string : ")
        upper_case, lower_case = string_upper_lower(sample_string)
        logger.info(f"String in uppercase: {upper_case} and lowercase: {lower_case}")
    except Exception as e:
        logger.error(f"{e} is raised")


if __name__ == "__main__":
    main()
