"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : List Data Structure Programs - Removing duplicates from List of Lists
    """


def remove_duplicates_list_of_lists(given_list):
    """
    Description :
        Removes duplicates from a list of lists.
    Parameters :
        given_list: Given list of lists from which the duplicates are to be removed.
    Return :
        Returns list of list without duplicates elements.
    """
    unique_list = []
    for element in given_list:
        if element not in unique_list:
            unique_list.append(element)
    return sorted(unique_list)


def main():
    try:
        sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        print("List of Lists:", sample_list)
        print("List of Lists after removing duplicates:", remove_duplicates_list_of_lists(sample_list))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
