"""
    @Author: Mayank Anand
    @Date: 2022-03-19
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-19
    @Title: String Data Structure Programs - Suffix of String after Splitting
    """
import logger

logger = logger.logging_init('suffix_split')


def suffix_char(given_string):
    """
    Description:
        Splits the given string based on '-' seperator.
    Parameter:
        given_string: Given string that is to be split.
    Return:
        Suffix of string after '-' character.
    """
    return given_string.rsplit('-', 1)[-1]


def main():
    try:
        sample_string = 'https://www.w3resource.com/python-exercises'
        logger.info(f"Given String: {sample_string}")
        logger.info(f"The Last Part of String after separation is: {suffix_char(sample_string)}")
    except Exception as e:
        logger.error(f"{e} is raised")


if __name__ == "__main__":
    main()
