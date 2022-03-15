"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Sets Data Structure Programs - Maximum and Minimum Value in Set
    """


def main():
    try:
        set1 = (3, 5, 7, 9, 11, 13, 15, 17, 19)
        print("Set:", set1)
        print("Maximum value in set", max(set1))
        print("Minimum value in set", min(set1))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
