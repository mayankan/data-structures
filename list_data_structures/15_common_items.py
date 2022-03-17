"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : List Data Structure Programs - Checking common items in lists
    """
import logging


def common_items_list(list1,list2):
    """
    Description :
        Finds common items from two given lists.
    Parameters :
        list1: Given list compared to another list for common items.
        list2: Another Given list compared to another list for common items.
    Return :
        Common Items in Both given lists.
    """
    common_items = [element for element in list1 if element in list2]
    return common_items


def main():
    try:
        sample_list = ["apple", "banana", "cherry", "pie"]
        sample_list2 = ["blueberry", "pineapple", "orange", "pie"]
        print("List 1:", sample_list)
        print("List 2:", sample_list2)
        print("Common Items in List1 and List2:", common_items_list(sample_list, sample_list2))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
