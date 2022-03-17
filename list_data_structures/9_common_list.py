"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : List Data Structure Programs - Lists having at least one common element
    """


def common_list(given_list1, given_list2):
    """
    Description:
        Checks common elements in two given lists.
    Parameter:
        given_list1: First given list to check for common elements.
        given_list2: Second given list to check for common elements.
    Return:
        True if at least one common elements are there in both the lists else False.
    """
    for element in given_list1:
        if element in given_list2:
            return True
    return False


def main():
    try:
        sample_list = ["apple", "banana", "cherry", "pie"]
        sample_list2 = ["blueberry", "pineapple", "orange", "pie"]
        print("List 1:", sample_list)
        print("List 2:", sample_list2)
        print("Both lists have at least one common element") if common_list(sample_list, sample_list2) else print(
                                                                          "Both lists don't have any common element")
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
