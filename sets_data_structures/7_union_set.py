"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Sets Data Structure Programs - Union of two sets
    """


def union_set(set1, set2):
    """
    Description:
        Calculates union of values in Set 1 and values in Set 2.
    Parameters:
        set1: Set of certain values.
        set2: Set of another certain values.
    Return:
        All values present in both Set 1 and Set 2.
    """
    return set1 | set2


def main():
    try:
        set1 = {3, 5, 7, 9, 11, 13, 15, 17, 19}
        set2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
        print("Set 1: ", set1)
        print("Set 2: ", set2)
        print("Union of two sets is:", union_set(set1, set2))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
