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
    final_dict = {}
    for inv_dict in (dic1, dic2, dic3):
        final_dict.update(inv_dict)
    print("Concatenated Dictionary is:", final_dict)


if __name__ == "__main__":
    main()
