"""
    @Author: Mayank Anand
    @Date: 2022-03-19
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-19
    @Title : String Data Structure Programs - String's occurrences in a larger string
    """
import logger

logger = logger.logging_init('substring_occurrence')


def count_substr_occurrence(given_string, sub_str):
    """
    Description:
        Counts of occurrences of a substring in a string.
    Parameter:
        given_string: Given string on which the occurrences of the substring is to be counted.
        sub_str: The substring whose count is to be calculated in the given string.
    Return:
        Count of occurrences of a substring within a string.
    """
    return given_string.count(sub_str)


def main():
    try:
        sample_string = "Hi Mayank, How are you? Mayank: I am fine, Thankyou."
        logger.info("Given String", sample_string)
        check_occurrence = "Mayank"
        logger.info("Occurrence of {} in String is {}".format(check_occurrence,
                            count_substr_occurrence(sample_string, check_occurrence)))
    except Exception as e:
        logger.error("{} is raised".format(e))


if __name__ == "__main__":
    main()
