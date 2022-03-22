"""
    @Author: Mayank Anand
    @Date: 2022-03-17
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title: String Data Structure Programs - Character Frequency of String
    """
import logger

logger = logger.logging_init('char_frequency')


def char_frequency(given_string):
    """
    Description:
        Counts the number of occurrences for each character in the given string.
    Parameter:
        given_string: Given string whose character frequency is to be calculated.
    Return:
        Dictionary which contains unique characters from given string as key and number of occurrences
         of each character in given string as its value.
    """
    result_dict = {}
    for character in given_string :
        if character in result_dict.keys():
            result_dict[character] += 1
        else:
            result_dict[character] = 1
    return result_dict


def main():
    try:
        sample_string = "Mayank"
        logger.info(f"Given String: {sample_string}")
        logger.info(f"Character Frequency of Given String is: {char_frequency(sample_string)}")
    except Exception as e:
        logger.error(f"{e} is raised")


if __name__ == "__main__":
    main()
