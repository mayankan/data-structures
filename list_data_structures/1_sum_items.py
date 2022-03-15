"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : List Data Structure Programs - Sum of all items in the list
    """


def sum_items(list1):
    """
    Description :
        Computes the sum of elements in the list.
    Parameters :
        list1: The list by which sum of elements are to be computed.
    Return:
         Sum of elements in the given list.
    """
    try:
        sum_of_items = 0
        for item in list1:
            sum_of_items += item
        return sum_of_items
        # Alternate code to sum all the elements
        # return sum(list1)
    except Exception as e:
        print("{} is raised".format(e))


def main():
    try:
        list1 = [3, 5, 7, 9, 11, 13, 15, 17, 19]
        print("List:", list1)
        print("Sum of all elements of List:", sum_items(list1))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
