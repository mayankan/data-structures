"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : List Data Structure Programs - Multiple of all items in the list
    """


def multiple_items(list1):
    """
    Description :
        Computes the multiple of elements in the list.
    Parameters :
        list1: The list by which product of elements is to be computed.
    Return:
         Product(Multiple) of elements in the given list.
    """
    try:
        product_of_items = 1
        for item in list1:
            product_of_items *= item
        return product_of_items
    except Exception as e:
        print("{} is raised".format(e))


def main():
    try:
        list1 = [3, 5, 7, 9, 11, 13, 15, 17, 19]
        print("List:", list1)
        print("Multiple of all elements of List:", multiple_items(list1))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
