"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-14
    @Title : Dictionary Data Structure Programs - Iterating over dictionary using Key and Value pair .
    """


def main():
    dic1 = {1: 10, 2: 20}
    for key, value in dic1.items():
        print("No of values for {} is {}.".format(key, value))


if __name__ == "__main__":
    main()
