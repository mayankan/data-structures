"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs
    """


def check_no_list(list_nos, search_no):
    """
    Checks if search_no is present in tuple_nos or not.
    Parameters:
        list_nos: Number values in List to be searched in.
        search_no: Number to be searched in tuple_nos.
    Return:
        True if search_no is Present else False
    """
    try:
        for no in list_nos:
            if no == search_no:
                return "True"
        return "False"
    except Exception as e:
        print("{} is raised.".format(e))


def main():
    try:
        list_nos = input("Enter numbers to search in separated by comma: ").split(",")
        search_no = input("Enter number to search in the above list: ")
        print(check_no_list(list_nos, search_no))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
