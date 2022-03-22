"""
    @Author: Mayank Anand
    @Date: 2022-03-19
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-19
    @Title: String Data Structure Programs - Print Longest Word in String List
    """
import logger

logger = logger.logging_init('longest_word')


def longest_word(word_list):
    """
    Description:
        Searches the longest word in a given list of words and returns the word, and it's length.
    Parameter:
        word_list: Given list of words in which the longest word is to be fetched.
    Return:
        Word with the longest length amongst the given list of words along with the length of that word.
    """
    try:
        longest_length = len(word_list[0])
        first_word = word_list[0]
        for word in word_list:
            if len(word) > longest_length:
                longest_length = len(word)
                first_word = word
        return first_word, longest_length
    except Exception as e:
        print("{} is raised.".format(e))


def main():
    try:
        sample_list = ["blueberry", "pineapple", "orange", "pie"]
        logger.info(f"Word List: {sample_list}")
        word_str, word_len = longest_word(sample_list)
        logger.info(f"Longest Word in List: {word_str} and it's length: {word_len}")
    except Exception as e:
        logger.error(f"{e} is raised")


if __name__ == "__main__":
    main()
