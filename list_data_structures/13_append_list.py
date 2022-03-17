"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : List Data Structure Programs - Appending one list to another list
    """


def main():
    try:
        sample_list = ["apple", "banana", "cherry", "pie"]
        sample_list2 = ["blueberry", "pineapple", "orange", "pie"]
        print("List 1:", sample_list)
        print("List 2:", sample_list2)
        sample_list.extend(sample_list2)
        print("List 2 after appending to List 1:", sample_list)
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
