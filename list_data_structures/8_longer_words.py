"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : List Data Structure Programs - Words longer than n in list
    """


def words_longer_than_n(given_list, no_of_characters):
    """
    Description:
        Checks elements in given list greater than given number of characters.
    Parameter:
        given_list: Given list to check words with greater than given number of characters.
        no_of_characters: Given number of characters to check elements in list.
    Return:
        List of elements with elements greater than given number of characters.
    """
    result_list = []
    for element in given_list:
        if len(element) > no_of_characters:
            result_list.append(element)
    return result_list


def main():
    try:
        sample_list = ["apple", "banana", "cherry", "blueberry", "pineapple", "orange", "pie"]
        print("List:", sample_list)
        no_of_chars = int(input("Enter n number greater than which you want the words in the list to be fetched: "))
        print("List with words greater than n:", words_longer_than_n(sample_list, no_of_chars))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
