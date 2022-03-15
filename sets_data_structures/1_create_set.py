"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Sets Data Structure Programs - Create a set
    """


def create_set():
    """
    Description:
        Creates set using set function and curly braces {}.
    Return:
        set with random values.
    """
    # Method 1
    set1 = set()
    set1 = {3, 5, 7, 9}
    # Method 2
    return set1


def main():
    set1 = create_set()
    print("Set:", set1)


if __name__ == "__main__":
    main()
