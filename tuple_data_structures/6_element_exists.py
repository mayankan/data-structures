"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : Tuple Data Structure Programs - Check item in tuple exists or not
    """


def item_exists(given_tuple, item):
    """
    Description :
        Checks the existence of an item in a tuple.
    Parameter :
        given_tuple: Given tuple in which given item has to be checked for it's existence.
        item: The item given by user which has to be checked in given tuple whether it exists or not.
    Return :
        Returns True if present in the tuple else False.
    """
    return True if item in given_tuple else False


def main():
    sample_tuple = ('p','r','o','g','a','m','i','z')
    check_item = 'z'
    print("Item exists in tuple.") if item_exists(sample_tuple, check_item) else print("Item does not exist in tuple.")


if __name__ == "__main__":
    main()
