"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Sets Data Structure Programs - Symmetric Difference between two sets
    """


def main():
    try:
        set1 = {3, 5, 7, 9, 11, 13, 15, 17, 19}
        set2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
        print("Set 1: ", set1)
        print("Set 2: ", set2)
        print("Symmetric Difference between two sets is:\n", set1.symmetric_difference(set2), "\n",
              set2.symmetric_difference(set1))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
