"""
    @Author: Mayank Anand
    @Date: 2022-03-19
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-19
    @Title : String Data Structure Programs - Formatted text within limit of 50 characters
    """
import textwrap
import logger

logger = logger.logging_init('format_string')


def display_formatted_text(given_string):
    """
    Description:
        Displays formatted text(width=50) as output.
    Parameter:
        given_string: Given string by the user that is to be formatted.
    Return:
        The formatted string with width=50.
    """
    # textwrap.fill() is used to print out the output in separate rows according to the width given to the string
    return textwrap.fill(given_string, width=50)



def main():
    try:
        sample_text = "Python is a widely used high-level, general-purpose, interpreted,dynamic programming language." \
        "Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in " \
        "fewer lines of code than possible in languages such as C++ or Java."
        logger.info(display_formatted_text(sample_text))
    except Exception as e:
        logger.error("{} is raised".format(e))


if __name__ == "__main__":
    main()
