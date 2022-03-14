"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-14
    @Title : Dictionary Data Structure Programs - Removing Element from dictionary using key.
    """


def main():
    dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    print("Dictionary:", dic1)
    # Using delete method to delete an element from dictionary using key specification.
    del dic1[3]
    print("Dictionary after removing 3rd key:", dic1)


if __name__ == "__main__":
    main()
