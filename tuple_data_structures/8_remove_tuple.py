"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : Tuple Data Structure Programs - Removing item from tuple
    """


def remove_item(given_tuple, item):
    """
    Description :
        Removes given item present in given tuple.
    Parameter :
        given_tuple: Given tuple from which given item is to be removed.
        item: The item to be removed.
    Return :
        Tuple after removing the given item.
    """
    # Tuples are immutable, i.e. we cannot remove item from tuple.
    # Converting the tuple to list to remove item.
    converted_list = list(given_tuple)
    converted_list.remove(item)
    # Converting the list to tuple after removing item.
    return_tuple = tuple(converted_list)
    return return_tuple

def main():
    sample_tuple = ("Mayank", 3.17, 22, True)
    print("Given tuple:", sample_tuple)
    print("Tuple after removing 3.17 item:", remove_item(sample_tuple, 3.17))


if __name__ == "__main__":
    main()
