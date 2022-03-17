"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : List Data Structure Programs - Checking circularly identical lists
    """


def circularly_identical(list1, list2):
    """
    Description :
       Checks whether two given lists are circularly identical or not.
    Parameters :
        list1: given list compared to other given list to check for circularly identity.
        list2: another given list to check for circularly identity.
    Return :
        True if the two lists are circularly identical else False.
    """
    list1.extend(list1)
    for index in range(len(list1)):
        if list2 == list1[index: index + len(list2)]:
            return True
    return False


def main():
    try:
        sample_list = [1, 0, 0, 1]
        sample_list2 = [1, 1, 0, 0]
        print("Lists are circularly identical") if circularly_identical(sample_list, sample_list2) else print(
                                                                          "Lists are not circularly identical")
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
