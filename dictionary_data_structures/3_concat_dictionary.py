"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-14
    @Title : Dictionary Data Structure Programs - Merging multiple dictionaries into one dictionary.
    """


def main():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    # Adding Dictionary 2 to Dictionary 1.
    dic1.update(dic2)
    # Adding Dictionary 3 to merged Dictionary 1 and 2.
    dic1.update(dic3)
    print("Concatenated Dictionary is:", dic1)


if __name__ == "__main__":
    main()
