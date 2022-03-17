"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : List Data Structure Programs - Split list using first character in each element
    """


def split_list(given_list):
    """
    Description :
        Splits given list using first character of each element in list.
    Parameters :
        given_list: given list which is to be split using first character of each element.
    Return :
        list of list with each element split using first character of each element.
    """
    result_list = []
    for element in given_list:
        element = element[0] + "," + element[1:len(element)]
        result_list.append(element.split(','))
    # Returns first character and all other characters in a list, i.e. [ ['a', 'bc'], ['b', 'cd'] ..]
    return result_list


def main():
    try:
        sample_list = ["apple", "banana", "cherry", "pie"]
        print("List:", sample_list)
        print("List after splitting:", split_list(sample_list))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
