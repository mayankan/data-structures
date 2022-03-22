"""
    @Author: Mayank Anand
    @Date: 2022-03-17
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : String Data Structure Programs - Length of String
    """
import logger

logger = logger.logging_init('len_string')


def string_length(given_string):
    """
    Description :
        Calculates the length of the string and return it.
    Parameters :
        given_string: Given string whose length is to be calculated.
    Return:
        Returns length of the string.
    """
    return len(given_string)


def main():
    try:
        logger.info("Starting executing main function of Length of String Program.")
        sample_string = "Mayank"
        logger.info("Given String: {}".format(sample_string))
        logger.info("Length of Given String is: {}".format(string_length(sample_string)))
        logger.info("Length of String Program successfully executed.")
    except Exception as e:
        logger.error("{} is raised".format(e))


if __name__ == "__main__":
    main()
