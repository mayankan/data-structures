"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-16
    @Title : List Data Structure Programs - Count of elements in list
    which have same first and last character
    """


def count_matches(given_list):
    """
    Description :
        Counts elements in list which have same first and last character.
    Parameters :
        given_list: The list in which elements are to be counted with same first and last character.
    Return:
         Count of elements in list with same first and last character.
    """
    try:
        count = 0
        for element in given_list:
            if len(element) > 1 and element[0] == element[-1]:
                count += 1
        return count
    except Exception as e:
        print("{} is raised".format(e))


def main():
    try:
        list1 = ['abc', 'xyz', 'aba', '1221']
        print("List:", list1)
        print("Count of Elements with same first and last characters:", count_matches(list1))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
