"""
    @Author: Mayank Anand
    @Date: 2022-03-17
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : String Data Structure Programs - String's first character occurrences replacement
    """
import logger

logger = logger.logging_init('occurrence_replacement')


def replace_second_char(given_string):
    """
    Description:
        Replaces second and further occurrences of a first character in given string with '$'.
    Parameter:
        given_string: Given string on which the second and further occurrences
        of first character is replaced with '$'.
    Return:
        Resultant string with second and further occurrences of a first character in given string replaced with '$'.
    """
    first_char = given_string[0]
    result_string = given_string.replace(first_char,'$')
    result_string = first_char + result_string[1:]
    return result_string


def main():
    try:
        sample_string = "restart"
        logger.info("Given String:", sample_string)
        logger.info("String after replacement of first character occurrences with $:", replace_second_char(sample_string))
    except Exception as e:
        logger.error("{} is raised".format(e))


if __name__ == "__main__":
    main()
