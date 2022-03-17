"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : List Data Structure Programs - Clones/ Copies list
    """


def copy_list(given_list):
    """
    Description :
        Clones given list.
    Parameters :
        list1: The list that has to be cloned
    Return :
        Cloned list.
    """
    cloned_list = given_list
    return cloned_list


def main():
    try:
        sample_list = [3, 5, 7, 9, 11, 13, 14, 14, 15, 17, 19, 19]
        print("List:",sample_list)
        print("List after cloning:", copy_list(sample_list))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
